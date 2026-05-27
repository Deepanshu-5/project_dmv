print("Hello welcome to scholarship eligibility checker")
age=int(input("enter your age: "))
marks=float(input("enter your marks in 12th class: "))
if age>=20 and marks>=85:
    print("congratulations! you are eligible for scholarship.")
else:
    print("sorry, you are not eligible for scholarship.")