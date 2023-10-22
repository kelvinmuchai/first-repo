class BankAccount:
    def __init__(self,accountHolder):

        self.__balance=0
        self._name=accountHolder
        with open(self._name +'Ledger.txt','w') as ledgerFile:
            ledgerFile.write('All Transaction  details for ' + self._name +'\n')

            ledgerFile.write('Balance is 0\n')

    def deposit(self,amount):
        if amount <= 0:
            return 'we do not allow negative Deposits'
        self.__balance += amount
        with open(self._name + ' Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Deposit ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self.__balance) + '\n')


    def withdraw(self,amount):
        if self.__balance < amount or amount < 0:
            return 'Not enough in account ,or withdrawal is less than zero'
        self.__balance -= amount
        with open(self._name +' Ledger.txt','a') as ledgerFile:
            ledgerFile.write('withdraw '+ str(amount) +'\n')
            ledgerFile.write('Balance is ' + str(self.__balance)+'\n')

acct = BankAccount('samson') # We create an account for Alice.
acct.deposit(120) # _balance can be affected through deposit()
acct.withdraw(40) # _balance can be affected through withdraw()

acct1=BankAccount('simon')
acct1.deposit(100)
acct1.withdraw(50)

