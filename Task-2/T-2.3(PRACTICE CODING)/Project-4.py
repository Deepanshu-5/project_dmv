print("--factorial Calculator--:")

def factorial(a):
    if a==0 or a==1:
        return 1
    
    return a*factorial(a-1)

try:
    num=int(input("enter a number: "))
    if num<0:
        print("enter a valid number which is positive")
    else:
        result=factorial(num)
        print(f"Factorial: {result}")
except ValueError:
    print("enter a valid value")