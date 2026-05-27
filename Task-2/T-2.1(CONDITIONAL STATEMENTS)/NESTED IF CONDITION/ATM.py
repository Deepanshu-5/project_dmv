print("welcome to the ATM machine")
balance = 5000
withdraw_amount = float(input("enter the amount you want to withdraw: "))
if withdraw_amount<=balance:
    if withdraw_amount <=0 :
        print("please enter valid amnount")
    else:
        balance-=withdraw_amount
        print("your available balance is :",balance)
else:
    print("the amount you enter is more than available balance")
    