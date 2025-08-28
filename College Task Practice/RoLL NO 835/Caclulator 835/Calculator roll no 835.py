def calculator():
    while True:
        print("________Welcome to mini-calculator by Hammad Muntazir________")

        print("Press 1 for addition")
        print("Press 2 for subtraction")
        print("Press 3 for multiplication")
        print("Press 4 for division")
        print("Press 0 to exit")
        
        
        choice = input("Enter your choice: ")

        if choice == "1":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 + num2
            print("The result is:", result)


        elif choice == "2":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 - num2
            print("The result is:", result)


        elif choice == "3":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 * num2
            print("The result is:", result)


        elif choice == "4":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if num2 == 0:
                print("Division by zero is not allowed.")

            else:
                result = num1 / num2
                print("The result is:", result)


        elif choice == "0":
            print("Program has been exited")
            break

        else:
            print("Invalid choice. Please choose again.")
            print()

if __name__ == "__main__":
    calculator()
