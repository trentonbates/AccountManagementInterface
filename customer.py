from checking import Checking
from savings import Savings
from credit import Credit

class Customer:
    def __init__(self, input_user):
        self.username = input_user
        self.checking = self.setChecking()
        self.savings = self.setSavings()
        self.credit = self.setCredit()

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
    
    def setChecking(self):
        pass

    def getChecking(self):
        return self.checking
    
    def setSavings(self):
        pass

    def getSavings(self):
        return self.savings
    
    def setCredit(self):
        pass

    def getCredit(self):
        return self.credit
    
    username = property(getUsername, setUsername)
    checking = property(getChecking, setChecking)
    savings = property(getSavings, setSavings)
    credit = property(getCredit, setCredit)