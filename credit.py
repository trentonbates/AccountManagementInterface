from account import Account

class Credit(Account):
    def __init__(self, input_id, input_bal, input_limit):
        super().__init__(input_id, input_bal)
        self.credit_limit = self.setCreditLimit(input_limit)

    def setCreditLimit(self, input_limit):
        return input_limit

    def getCreditLimit(self):
        return self.credit_limit