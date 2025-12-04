class Account():
    def __init__(self, input_id, input_bal):
        self.account_id = self.setAccountId(input_id)
        self.balance = self.setBalance(input_bal)
        self.interest = 0.0

    def setAccountId(self, input_id):
        return input_id

    def getAccountId(self):
        return self.account_id

    def setBalance(self, input_bal):
        return input_bal

    def getBalance(self):
        return self.balance
    
    def __str__(self):
        pass