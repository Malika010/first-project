# main.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return float('inf')  # handle divide by zero
    return a / b

# Only run user input when the file is executed directly
if __name__ == "__main__":
    print("Select operation: +, -, *, /")
    operation = input("Enter operation: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        print("Result:", add(num1, num2))
    elif operation == '-':
        print("Result:", subtract(num1, num2))
    elif operation == '*':
        print("Result:", multiply(num1, num2))
    elif operation == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")
