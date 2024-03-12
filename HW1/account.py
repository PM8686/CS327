from comparable import ComparableMixin
import operator

class Account(ComparableMixin):
    """Represent a Account in the Accountbook. Match against a
    string in searches and store tags for each Account."""

    def __init__(self, account_type, id):
        """initialize an account with account type and unique id.
        Automatically set the account's empty list of transactions, balance = 0."""

        self._account_type = account_type
        self._transactions = []
        self._balance = 0
        self._id = id

    def id_matches(self, id):
        """
        Determine if this account has the given id
        """
        return self._id == int(id)

    def all_transactions(self):
        """Returns all transactions in the account in order by date"""

        self._transactions.sort(key=operator.attrgetter('_date'))
        return self._transactions

    def __str__(self):
        return (f"{self._account_type.capitalize()}#%09d," % (self._id) + "\tbalance: " +  f"${self._balance:,.2f}")
 
    def __lt__(self, other):
        return self._id < other._id