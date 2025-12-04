class Account():
    def __init__(self, input_id, input_bal):
        self.account_id = self.setAccountId(input_id)
        self.balance = self.setBalance(input_bal)
        self.interest = 0.0

    def setAccountId(self, input_id):
        if not isinstance(input_id, str):
            raise TypeError('AccountId needs to be a numerical string.')
        elif not len(input_id) == 4:
            raise ValueError('AccountId has to be exactly four numbers long.')
        elif not all(char in '0123456789' for char in input_id):
            raise ValueError('AccountId needs to only contain numbers from 0-9.')
        else:
            return input_id

    def getAccountId(self):
        return self.account_id

    def setBalance(self, input_bal):
        if not isinstance(input_bal, int) or not isinstance(input_bal, float):
            raise TypeError('Balance needs to be an int or a float.')
        elif input_bal < 0:
            raise ValueError('Balance cannot be negative.')
        else:
            self.balance = input_bal

    def getBalance(self):
        return self.balance
    
    def getInterest(self):
        return self.interest
    
    def __str__(self):
        return (f'AccountId: {self.getAccountId()}\n'
                + f'Balance: ${self.getBalance()}\n'
                + f'Interest: {self.getInterest() * 100}%\n')

    account_id = property(getAccountId, setAccountId)
    balance = property(getBalance, setBalance)