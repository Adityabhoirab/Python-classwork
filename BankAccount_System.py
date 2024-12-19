class BankAccount:
    def __int__(self,initialAmt,accName):
        self.balance=initialAmt
        self.name=accName 
        print("account create successfully")
        print(f"\n account for '{self.name}'is created with {self.balance:.2f}")
        
    def getBalance(self):
        print(f"Account created for:{self.name}\n")
        print(f"opening balance is :{self.balance}")
        
    def deposite(self,amount):
        self.balance=self.balance+amount
        print("amount deposited successfully")