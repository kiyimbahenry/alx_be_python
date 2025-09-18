# match_case_calculator.py
# Calculator using match-case statement

def main():
    # Prompt user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt user for operation
    operation = input("Choose the operation (+, -, *, /): ").strip()
    
    # Perform calculation using match-case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print("Invalid operation! Please choose from +, -, *, /")

# Run the program
if __name__ == "__main__":
    main()
