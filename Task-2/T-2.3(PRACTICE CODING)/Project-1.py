print("---this is the grade calculator---:")

def grade_calc(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"
try:
    marks = float(input("Enter your marks: "))
    if marks < 0 or marks > 100:
        print("Invalid marks. Enter between 0 and 100")
    else:
        grade = grade_calc(marks)
        print(f" Grade : {grade}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
    


