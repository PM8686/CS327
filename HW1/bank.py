from account import Account

class Bank:
    """Represent a collection of Accounts that can be tagged,
    modified, and searched."""

    def __init__(self):
        """Initialize a Bank with an empty list and 
        the variable that keeps track of the last unique 
        id used for accounts."""

        self._bank = []
        # Stores the next available id for all new Accounts
        self._last_id = 0

    def new_account(self, account_type):
        """Create a new account and add it to the list."""
        self._last_id += 1
        n = Account(account_type, self._last_id)
        self._bank.append(n)
        return n

    def _find_account(self, account_id):
        """Locate the account with the given id."""
        for account in self._bank:
            if account.id_matches(account_id):
                return account
        return None

    def all_accounts(self):
        """Returns all accounts in the bank sorted"""

        self._bank.sort()
        return self._bank
