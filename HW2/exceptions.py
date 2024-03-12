class OverdrawError(Exception):
    """Raised when the user attempts to withdraw more money than they have in the account"""
    pass


class TransactionSequenceError(Exception):
    """Raised when the new transaction would have a date older than the latest transaction
    Or if interest was already calculated for the given month"""

    def __init__(self, date, error_type):
        self.latest_date = date
        self.error = error_type


class TransactionLimitError(Exception):
    """Raised when the user has reached the transaction limit on the savings account"""

    def __init__(self, limit_type, limit_amount):
        self.type = limit_type
        self.amount = limit_amount
