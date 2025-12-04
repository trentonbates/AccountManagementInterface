from account import Account

class Savings(Account):
    def __init__(self, input_id, input_bal):
        super().__init__(input_id, input_bal)
        self.interest = 0.3