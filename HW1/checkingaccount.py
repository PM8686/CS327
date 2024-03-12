class CheckingAccount:

    # interest for checking accounts
    checking_interest = .0008
    # fee for interest calculation on acct with < $100
    low_funds_fee = -5.44

    def _checking_interest(account):
        """calculate the interest for the given checking account"""

        interest = account._balance * CheckingAccount.checking_interest
        account._balance += interest
        return interest

    def _interest_fee(account):
        """determine whether or not to apply the interest fee"""

        if account._balance < 100:
            account._balance += CheckingAccount.low_funds_fee
            return CheckingAccount.low_funds_fee
        return None