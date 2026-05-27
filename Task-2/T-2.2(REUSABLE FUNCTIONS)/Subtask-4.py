print("Understand Function Scope\n")

a=float(input("Enter a value for a: "))
b=float(input("Enter a value for b: "))

def fun():
    a=200
    c=a-b
    print("The value of a - b is: ",c)
    print("The value of a in local scope is: ",a)
    
fun()
print("The value of a  in global scope is: ",a)
