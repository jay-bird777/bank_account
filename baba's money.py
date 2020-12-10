







def compound_interest():
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
compound_interest()
