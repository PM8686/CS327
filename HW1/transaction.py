from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount
import calendar

class Transaction:
    """Represent a transaction recording the amount deposited/withdrawn
    and the date the transaction occured."""

    def __init__(self, amount, date, interest_flag=False):
        """initialize transaction with an amount, a date, and automatically assign interest_flag to False"""
        self._amount = float(amount)
        self._date = date
        self._interest_flag = interest_flag
    
    def _transaction_check_balance(self, account):
        """check if the transaction with over-withdraw from the given account"""
        if self._amount < 0:
            if -1*self._amount > account._balance:
                return False
        return True

    def _transaction_count(self, account):
        """check if the transaction limit/day or /week has been reached"""
        if account._account_type == "checking":
            return True
        return SavingsAccount._savings_transaction(self, account)

    def _transaction_check(self, account):
        """ensures that the transaction does not violate predetermined rules"""
        return self._transaction_check_balance(account) and self._transaction_count(account)
    
    def _interest_date(account):
        """finds the date for the interest transaction/
        the last day of the month on the most future transaction"""
        transactions = account.all_transactions()
        latest_transaction = transactions[-1]
        date = latest_transaction._date.split("-")
        month_last_day = calendar.monthrange(int(date[0]), int(date[1]))
        date[2] = str(month_last_day[1])
        return date
    
    def _interest_fees(account):
        """calculates interest and fees on the selected account"""

        # input transaction date for interest/fee (last day of the month of most future transaction)
        date = Transaction._interest_date(account)

        # # input transaction amount
        if account._account_type == "checking":
            interest = CheckingAccount._checking_interest(account)
        else: 
            interest = SavingsAccount._savings_interest(account)

        # add transaction to the account
        account._transactions.append(Transaction(interest, '-'.join(i for i in date), True))

        # check if fees need to be added
        if account._account_type == "checking":
            fee = CheckingAccount._interest_fee(account)
            if fee is not None:
                account._transactions.append(Transaction(fee,  '-'.join(i for i in date)))
    
    def __str__(self):
        return (f"{self._date}, ${self._amount:,.2f}")