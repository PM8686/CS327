import sys
import pickle
from bank import Bank
from decimal import Decimal
from transaction import Transaction

class Menu:
    """Display a menu and respond to choices when run."""

    # Store the currently selected account
    selected_account = None

    def __init__(self):
        """initialize menu with options"""
        self._bank = Bank()
        self._choices = {
            "1": self._open_account,     
            "2": self._summary,          
            "3": self._select_account,   
            "4": self._add_transaction,  
            "5": self._list_transactions,
            "6": self._interest_fees,    
            "7": self._save,                 
            "8": self._load,                
            "9": self._quit,                
        }
        
    def _display_menu(self):
        print(
"""--------------------------------
Currently selected account: %s
Enter command
1: open account
2: summary
3: select account
4: add transaction
5: list transactions
6: interest and fees
7: save
8: load
9: quit""" % (Menu.selected_account))

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self._display_menu()
            choice = input(">")
            action = self._choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def _open_account(self, account_type=None):
        """open a new account"""

        account_type = input("Type of account? (checking/savings)\n>")
        self._bank.new_account(account_type)


    def _summary(self, accounts=None):
        """display a sorted list of the accounts created in the bank"""
        if accounts is None:
            accounts = self._bank.all_accounts()
        for account in accounts:
            Decimal(account._balance).quantize(Decimal('.01'), rounding='ROUND_HALF_UP')
            print(str(account))


    def _select_account(self):
        account_id = input("""Enter account number\n>""")
        Menu.selected_account = self._bank._find_account(account_id)

    def _add_transaction(self):
        """adds a transaction to the user selected account"""
        amount = float(input("Amount?\n>"))
        date = input("Date? (YYYY-MM-DD)\n>")
        n = Transaction(amount, date)
        if not n._transaction_check(Menu.selected_account):
            return
        Menu.selected_account._transactions.append(n)
        Menu.selected_account._balance += amount

    def _list_transactions(self, transactions=None):
        """display a list of transactions of the selected account"""
        if transactions is None:
            transactions = Menu.selected_account.all_transactions()
        for transaction in transactions:
            Decimal(transaction._amount).quantize(Decimal('.01'), rounding='ROUND_HALF_UP')
            print(str(transaction))

    def _interest_fees(self):
        """calculate interest and fees associated with the account"""
        Transaction._interest_fees(Menu.selected_account)


    def _save(self):
        with open("Bank_save.pickle", "wb") as f:
            pickle.dump(self._bank, f)

    def _load(self):
        with open("Bank_save.pickle", "rb") as f:   
            self._bank = pickle.load(f)

    def _quit(self):
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
