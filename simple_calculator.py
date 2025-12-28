print("=" * 40)
print("        🧮 SIMPLE CALCULATOR")
print("=" * 40)

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("-" * 40)
        print("Thank you for using the calculator 👋")
        print("-" * 40)
        break

    if choice not in ["1", "2", "3", "4"]:
        print("❌ Invalid choice. Please select between 1-5.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)

        elif choice == "2":
            print("Result:", num1 - num2)

        elif choice == "3":
            print("Result:", num1 * num2)

        elif choice == "4":
            if num2 == 0:
                print("❌ Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)

    except ValueError:
        print("❌ Please enter valid numbers only.")
