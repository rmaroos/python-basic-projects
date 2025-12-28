print("=" * 45)
print("        🌡️ TEMPERATURE CONVERTER")
print("=" * 45)

while True:
    print("\nChoose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")
    
    if choice == "3":
        print("-" * 45)
        print("Thank you for using the Temperature Converter 👋")
        print("-" * 45)
        break

    if choice not in ["1", "2"]:
        print("❌ Invalid choice. Please select 1, 2, or 3.")
        continue

    try:
        temp = float(input("Enter temperature value: "))

        if choice == "1":
            fahrenheit = (temp * 9/5) + 32
            print(f"{temp}°C = {fahrenheit:.2f}°F")

        elif choice == "2":
            celsius = (temp - 32) * 5/9
            print(f"{temp}°F = {celsius:.2f}°C")

    except ValueError:
        print("❌ Please enter a valid numeric temperature.")