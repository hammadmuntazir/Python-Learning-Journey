while True:  # This creates an infinite loop
    marks = int(input("Enter marks: "))

    print(marks)

    if marks % 5 == 0:
        print(marks, "is divisible by 5")
    elif marks % 3 == 0:
        print(marks, "is divisible by 3")
    else:
        print(marks, "is not divisible by 3 or 5")

    again = input("Do you want to enter another number? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Exiting the program. Goodbye!")
        break