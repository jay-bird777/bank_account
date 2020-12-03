class Bank_Account:
    
    def __init__(self):
        self.balance = 0
        print("my balance is 0 ")
        
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n amount being deposited: ", amount)
        
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n amount being withdrawn: ", amount)
        else:
            print("\n insufficient balance ")
            
    def display(self):
        print("\n net available balance=", self.balance)
        
#creating an object of class
baba = Bank_Account()
#Calling that function with that object
baba.deposit()
baba.withdraw()
baba.display()
        
    
        
        
