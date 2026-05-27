print("Hello welcome to loan eligibility checker")
age = int(input("enter your age: "))
income = float(input("enter your annual income: "))
credit_score = int(input("enter your credit score: "))
if age >= 18 and income >= 30000 and credit_score >= 700:
    print("congratulations! you are eligible for a loan.")
else:
    print("sorry, you are not eligible for a loan.")