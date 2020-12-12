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

    def compound_interest(self):
        p = float(input("what is the principle? "))
        r = float(input("what is the rate? "))
        n = int(input("how many payments per year? "))
        t = int(input("how many years? "))
        pv = p * (pow((1 + r/100/n),n*t))
        balance = p * (pow((1 + r/100/n),n*t))
        ci = balance - p
        print('Balance at the end of the period',round(balance,2))
        print("Intrest earned is", round(ci,2))
        roi = (ci/balance) * 100
        print("This is", round(roi,2),"% return on investment.")
        
    def mortgage_payment(self, n, rate):
        p = self.balance*(rate/12/100*pow((1+rate/12/100), n))/(pow((1+rate/12/100),n)-1)
        print(round(p,2))
#creating an object of class
baba = Bank_Account()
#Calling that function with that object
baba.deposit()
baba.withdraw()
baba.display()
baba.compound_interest()
baba.mortgage_payment(360, 2.875)
    
        
        
