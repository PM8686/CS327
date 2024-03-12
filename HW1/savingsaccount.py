class SavingsAccount:
    
    # interest for saving accounts
    savings_interest = .0041

    def _savings_transaction(self, account):
        """check if the transaction can go through/
        if transactions/day or transactions/month limit has been reached"""
        count_day = 0
        count_month = 0
        for transaction in account._transactions:
            # if transaction is not a part of an interest transaction
            if transaction._interest_flag == False:
                # check transactions/day limit
                if self._date == transaction._date:
                    count_day += 1
                    if count_day > 1:
                        return False
                # check transactions/month limit
                if self._date.split("-")[1] == transaction._date.split("-")[1]:
                    count_month += 1
                    if count_month > 4:
                        return False
        return True
    
    def _savings_interest(account):
        """calculates interest for a savings account"""
        interest = account._balance * SavingsAccount.savings_interest
        account._balance += interest
        return interest