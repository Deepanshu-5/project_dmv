print("determine your bonus eligibility")
performance = float(input("enter your performance score: "))
attendance = float(input("enter your attendance percentage: "))
years= int(input("enter your years of service: "))
if performance >= 80:
    if attendance >= 75:
        if years >= 2:
            print("you are eligible for a bonus!")
        else:
            print("you are not eligible due to less years of service.")
    else:
        print("you are not eligible due to low attendance.")
else:
    print("you are not eligible for a bonus.")