from decimal import Decimal
import logging

from transactions import Transaction
from exceptions import TransactionLimitError, TransactionSequenceError


class Account:
    """This is an abstract class for accounts.  Provides default functionality for adding transactions, getting balances, and assessing interest and fees.  
    Accounts should be instantiated as SavingsAccounts or CheckingAccounts
    """

    def __init__(self, acct_num):
        self._transactions = []
        self._account_number = acct_num

    def _get_acct_num(self):
        return self._account_number

    account_number = property(_get_acct_num)

    def add_transaction(self, amt, date, exempt=False):
        """Creates a new transaction and checks to see if it is allowed, adding it to the account if it is.

        Args:
            amt (Decimal): amount for new transaction
            date (Date): Date for the new transaction.
            exempt (bool, optional): Determines whether the transaction is exempt from account limits. Defaults to False.
        """

        t = Transaction(amt,
                        date,
                        exempt=exempt)

        # Logic is broken up into pieces and factored out into other methods.
        # This makes it easier to override specific parts of add_transaction.
        # This is called a Template Method design pattern
        balance_ok = self._check_balance(t)
        limits_ok = self._check_limits(t)

        # returns an error if the new transaction's date is before the most current date
        if self._transactions:
            latest_transaction = max(self._transactions)
            if t._date < latest_transaction._get_transaction_date():
                raise TransactionSequenceError(
                    latest_transaction._get_transaction_date(), "transaction")

        if t.is_exempt() or (balance_ok and limits_ok):
            self._transactions.append(t)

    def _check_balance(self, t):
        """Checks whether an incoming transaction would overdraw the account

        Args:
            t (Transaction): pending transaction

        Returns:
            bool: false if account is overdrawn
        """
        return t.check_balance(self.get_balance())

    def _check_limits(self, t):
        return True

    def get_balance(self):
        """Gets the balance for an account by summing its transactions

        Returns:
            Decimal: current balance
        """
        # could have a balance variable updated when transactions are added (or removed) which is faster
        # but this is more foolproof since it's always in sync with transactions
        # this could be improved by caching the sum to avoid too much
        # recalculation, while still maintaining the list as the ground truth
        return sum(self._transactions)

    def _assess_interest(self, latest_transaction):
        """Calculates interest for an account balance and adds it as a new transaction exempt from limits.
        """
        interest_added = self.get_balance() * self._interest_rate
        self.add_transaction(interest_added,
                             date=latest_transaction.last_day_of_month(),
                             exempt=True)
        logging.debug("Created transaction: %i, %f",
                      self._get_acct_num(), interest_added)

    def _assess_fees(self, latest_transaction):
        pass

    def assess_interest_and_fees(self):
        """Used to apply interest and/or fees for this account"""
        # gives an error if there has already been an interest calculation for the month
        if self._transactions:
            latest_transaction = max(self._transactions)
            for transaction in self._transactions:
                if latest_transaction.in_same_day(transaction) and transaction.is_exempt():
                    raise TransactionSequenceError(
                        latest_transaction._get_transaction_date(), "interest")

        self._assess_interest(latest_transaction)
        self._assess_fees(latest_transaction)

        # If no exception was created, then log the interest and fees addition
        logging.debug("Triggered interest and fees")

    def __str__(self):
        """Formats the account number and balance of the account.
        For example, '#000000001,<tab>balance: $50.00'
        """
        return f"#{self._account_number:09},\tbalance: ${self.get_balance():,.2f}"

    def get_transactions(self):
        "Returns sorted list of transactions on this account"
        return sorted(self._transactions)


class SavingsAccount(Account):
    """Concrete Account class with daily and monthly account limits and high interest rate.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._interest_rate = Decimal("0.0041")
        self._daily_limit = 2
        self._monthly_limit = 5

    def _check_limits(self, t1):
        """determines if the incoming trasaction is within the accounts transaction limits

        Args:
            t1 (Transaction): pending transaction to be checked

        Returns:
            bool: true if within limits and false if beyond limits
        """
        # Count number of non-exempt transactions on the same day as t1
        num_today = len(
            [t2 for t2 in self._transactions if not t2.is_exempt() and t2.in_same_day(t1)])
        # Count number of non-exempt transactions in the same month as t1
        num_this_month = len(
            [t2 for t2 in self._transactions if not t2.is_exempt() and t2.in_same_month(t1)])
        # check counts against daily and monthly limits
        if (num_today >= self._daily_limit):
            raise TransactionLimitError("day", self._daily_limit)
        elif (num_this_month >= self._monthly_limit):
            raise TransactionLimitError("month", self._monthly_limit)

        return True

    def __str__(self):
        """Formats the type, account number, and balance of the account.
        For example, 'Savings#000000001,<tab>balance: $50.00'
        """
        return "Savings" + super().__str__()


class CheckingAccount(Account):
    """Concrete Account class with lower interest rate and low balance fees.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._interest_rate = Decimal("0.0008")
        self._balance_threshold = 100
        self._low_balance_fee = Decimal("-5.44")

    def _assess_fees(self, latest_transaction):
        """Adds a low balance fee if balance is below a particular threshold. Fee amount and balance threshold are defined on the CheckingAccount.
        """
        if self.get_balance() < self._balance_threshold:
            self.add_transaction(self._low_balance_fee,
                                 date=latest_transaction.last_day_of_month(),
                                 exempt=True)
            logging.debug("Created transaction: %i, %f",
                          self._get_acct_num(), self._low_balance_fee)

    def __str__(self):
        """Formats the type, account number, and balance of the account.
        For example, 'Checking#000000001,<tab>balance: $50.00'
        """
        return "Checking" + super().__str__()
