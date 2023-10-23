
def calculator():
    while True:
        # Ask the user to enter two numbers and an operator
        num1 = input("Enter the first number: ")
        if num1 == 'q':
            break
        num2 = input("Enter the second number: ")
        if num2 == 'q':
            break
        operator = input("Enter an operator (+, -, *, /): ")

        # Check which operator was entered and perform the corresponding operation
        if operator == '+':
            result = float(num1) + float(num2)
        elif operator == '-':
            result = float(num1) - float(num2)
        elif operator == '*':
            result = float(num1) * float(num2)
        elif operator == '/':
            if num2 == '0':
                print("Error: division by zero")
                continue
            result = float(num1) / float(num2)
        else:
            print("Error: invalid operator")
            continue

        # Print the result of the operation
        print(f"{num1} {operator} {num2} = {result}")


calculator()

# The program should continue until the user enters 'q' to quit.
