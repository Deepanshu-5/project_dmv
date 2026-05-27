print("welcome to \"jatka college\" ")
marks = float(input("enter your marks in 12th standard"))
age = int(input("enter your age"))
if marks >= 60:
    if age >= 18:
        print("you are eligible for admission")
    else:
        print("you are not eligible for admission due to age")
else:
    print("you are not eligible for admission due to marks")