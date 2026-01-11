def trim_zeros(num):
    if num.is_integer():
        return int(num)
    return num

def operation(a, b, operation_type):
    match operation_type:
        case "1":
            return trim_zeros(a + b)
        case "2":
            return trim_zeros(a - b)
        case "3":
            return trim_zeros(a * b)
        case "4":
            if b != 0:
                return trim_zeros(a / b)
            else:
                return "Error: Division by zero."

def main():
    print("========Welcome to the Calculator Program========")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    # play = True
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ["1", "2", "3", "4"]:
            while True:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.\n")
            print(operation(num1, num2, choice))
            ask = input("Do you want to perform another operation? (y(default)/n): ").lower()
            if ask != "y" and ask != "":
                # play = False
                print("Thank you for using the calculator. Goodbye!")
                break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
