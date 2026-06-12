import math
def menu():
    print("\n=== Scientific Calculator ===")
    print("Binary: +, -, *, /, ^")
    print("Trigonometry: sin, cos, tan")
    print("Other: sqrt, log")
    print("Conversion: deg, rad")
    print("Type 'exit' to quit")
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y,
    'sin': lambda x: math.sin(x),
    'cos': lambda x: math.cos(x),
    'tan': lambda x: math.tan(x),
    'sqrt': lambda x: math.sqrt(x),
    'log': lambda x: math.log(x),
    'deg': lambda x: math.degrees(x),
    'rad': lambda x: math.radians(x)
}
def get_number(prompt):
    value = input(prompt).strip().lower()
    if value == 'pi':
        return math.pi
    return float(value)
def main():
    while True:
        menu()
        choice = input("Enter operation: ").strip().lower()
        if choice == 'exit':
            print("Goodbye!")
            break
        if choice not in operations:
            print("Invalid operation")
            continue
        
        unary_operations = ['sin', 'cos', 'tan','sqrt', 'log', 'deg', 'rad']
        try:
            if choice in unary_operations:
                num = get_number("Enter number (or pi): ")
                result = operations[choice](num)
            else:
                num1 = get_number("Enter first number (or pi): ")
                num2 = get_number("Enter second number (or pi): ")
                if choice == '/' and num2 == 0:
                    print("Cannot divide by zero")
                    continue
                result = operations[choice](num1, num2)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid numeric input")

        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    main()
