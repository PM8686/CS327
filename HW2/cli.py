import sys
import pickle
import logging

from decimal import Decimal, setcontext, BasicContext, InvalidOperation
from datetime import datetime
from transactions import OverdrawError
from accounts import TransactionSequenceError, TransactionLimitError
from bank import Bank


# context with ROUND_HALF_UP
setcontext(BasicContext)


class BankCLI:
    """Driver class for a command-line REPL interface to the Bank application"""

    def __init__(self):
        self._bank = Bank()

        # establishes relationship to Accounts
        self._selected_account = None

        self._choices = {
            "1": self._open_account,
            "2": self._summary,
            "3": self._select,
            "4": self._add_transaction,
            "5": self._list_transactions,
            "6": self._monthly_triggers,
            "7": self._save,
            "8": self._load,
            "9": self._quit,
        }

    def _display_menu(self):
        print(f"""--------------------------------
Currently selected account: {self._selected_account}
Enter command
1: open account
2: summary
3: select account
4: add transaction
5: list transactions
6: interest and fees
7: save
8: load
9: quit""")

    def run(self):
        """Display the menu and respond to choices."""

        while True:
            self._display_menu()
            choice = input(">")
            action = self._choices.get(choice)
            # expecting a digit 1-9
            if action:
                action()
            else:
                # not officially part of spec since we don't give invalid options
                print("{0} is not a valid choice".format(choice))

    def _summary(self):
        # dependency on Account objects
        for x in self._bank.show_accounts():
            print(x)

    def _load(self):
        with open("bank.pickle", "rb") as f:
            self._bank = pickle.load(f)
        logging.debug("Loaded from bank.pickle")

        # clearing the selected account so it doesn't get out of sync 
        # with the new account objects loaded from the pickle file
        self._selected_account = None

    def _save(self):
        with open("bank.pickle", "wb") as f:
            pickle.dump(self._bank, f)
        logging.debug("Saved to bank.pickle")

    def _quit(self):
        sys.exit(0)

    def _add_transaction(self):

        # Askes the user to input the amount until the user inputs a valid dollar amount
        while True:
            try:
                amount = input("Amount?\n>")
                amount = Decimal(amount)  # convert to Decimal
                break
            except InvalidOperation:
                print("Please try again with a valid dollar amount.")

        # loops until the user inputs the date correctly
        while True:
            try:
                date = input("Date? (YYYY-MM-DD)\n>")
                date = datetime.strptime(
                    date, "%Y-%m-%d").date()  # convert to date
                break
            # print an error message if the date was entered wrong
            except ValueError:
                print("Please try again with a valid date in the format YYYY-MM-DD.")

        try:
            self._selected_account.add_transaction(amount, date)
        # print an error message if no account was selected
        except AttributeError:
            print("This command requires that you first select an account.")
            return
        # returns an error if the user tries to withdraw more money than is in the account
        except OverdrawError:
            print(
                "This transaction could not be completed due to an insufficient account balance.")
            return
        # returns an error if the account reached its transaction limit for the day or month
        except TransactionLimitError as limit:
            print(
                f"This transaction could not be completed because this account already has {limit.amount} transactions in this {limit.type}.")
            return
        # returns an error if the user inputted transaction has a date before the most future date.
        except TransactionSequenceError as date:
            print(f"New transactions must be from {date.latest_date} onward.")
            return

        logging.debug("Created transaction: %i, %f",
                      self._selected_account._get_acct_num(), amount)

    def _open_account(self):
        acct_type = input("Type of account? (checking/savings)\n>")
        self._bank.add_account(acct_type)

    def _select(self):
        num = int(input("Enter account number\n>"))
        self._selected_account = self._bank.get_account(num)

    def _monthly_triggers(self):
        try:
            self._selected_account.assess_interest_and_fees()
        # print an error message if no account was selected
        except AttributeError:
            print("This command requires that you first select an account.")
        # returns an error if interest was already found for the month
        except TransactionSequenceError as date:
            print(
                f"Cannot apply interest and fees again in the month of {date.latest_date.strftime('%B')}.")

    def _list_transactions(self):
        try:
            for t in self._selected_account.get_transactions():
                print(t)
        # print an error message if no account was selected
        except AttributeError:
            print("This command requires that you first select an account.")


if __name__ == "__main__":
    try:
        logging.basicConfig(filename='bank.log', level=logging.DEBUG,
                            format='%(asctime)s|%(levelname)s|%(message)s', datefmt='%Y-%m-%d %I:%M:%S')
        BankCLI().run()
    except Exception as err:
        logging.error("%s: %s", type(err).__name__, err)
        print("Sorry! Something unexpected happened. Check the logs or contact the developer for assistance.")
