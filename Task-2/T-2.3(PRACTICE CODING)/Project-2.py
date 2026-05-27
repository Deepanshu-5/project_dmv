print("Temperature Converter (Celsius to Fahrenheit)")

def temp(C):
    F=(C*9/5)+32
    return F
    
try:
    celcius=float(input("Enter temperature: "))
    Fahrenheit=temp(celcius)
    
    print(f"Temperature in Fahrenheit: {Fahrenheit}F")
except ValueError:
    print("please enter valid values")