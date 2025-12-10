from checking import Checking
from savings import Savings
from credit import Credit

class Customer:
    def __init__(self, input_user, input_checking, input_savings, input_credit):
        self.username = input_user
        self.checking = input_checking
        self.savings = input_savings
        self.credit = input_credit

    def setUsername(self, input_user):
        alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
        if not isinstance(input_user, str):
            raise TypeError('Username must be a string.')
        elif not all(char.lower() in alpha for char in input_user):
            raise ValueError('Username must only contain letters and numbers.')
        else:
            self._username = input_user

    def getUsername(self):
        return self.username
    
    def setChecking(self, input_checking):
        if not isinstance(input_checking, Checking):
            raise TypeError('Checking account data is invalid.')
        else:
            self._checking = input_checking

    def getChecking(self):
        return self.checking
    
    def setSavings(self, input_savings):
        if not isinstance(input_savings, Savings):
            raise TypeError('Savings account data is invalid.')
        else:
            self._savings = input_savings

    def getSavings(self):
        return self.savings
    
    def setCredit(self, input_credit):
        if not isinstance(input_credit, Credit):
            raise TypeError('Credit account data is invalid.')
        else:
            self._credit = input_credit

    def getCredit(self):
        return self.credit
    
    def __str__(self):
        result = f'Customer: {self.username}' 
        + print(self.checking) 
        + print(self.savings)
        + print(self.credit)

        return result
    
    username = property(getUsername, setUsername)
    checking = property(getChecking, setChecking)
    savings = property(getSavings, setSavings)
    credit = property(getCredit, setCredit)