from account import Account

class Credit(Account):
    def __init__(self, input_id, input_bal, input_limit):
        super().__init__(input_id, input_bal)
        self.interest = 0.3
        self.credit_limit = input_limit

    def setCreditLimit(self, input_limit):
        if not isinstance(input_limit, (int, float)):
            raise TypeError('Credit limit needs to be an int or a float.')
        elif input_limit < 0:
            raise ValueError('Credit limit cannot be negative.')
        # elif input_limit < self.getBalance():
        #     raise ValueError('Credit limit cannot be lower than the current balance.')
        else:
            self._credit_limit = input_limit

    def getCreditLimit(self):
        return self.credit_limit
    
    def __str__(self):
        return 'Account Type: Credit\n' + super().__str__() + f'Credit Limit: ${self.getCreditLimit}\n'

    credit_limit = property(getCreditLimit, setCreditLimit)