print("=" * 45)
print("        🔐 BMI CALCULATOR 🔐")
print("=" * 45)
print()

# User Inputs
height = float(input(" Enter your height in meters (e.g. 1.62): "))
weight = float(input(" Enter your weight in kilograms (e.g. 55): "))
print()

# BMI Calculation
bmi = weight / (height ** 2)

# BMI Result
print("-" * 45)
print(f"📊 Your BMI is : {bmi:.2f}")
print("-" * 45)

# BMI Category
if bmi < 18.5:
    print("🟡 Category : Underweight")
elif 18.5 <= bmi < 25:
    print("🟢 Category : Normal weight")
elif 25 <= bmi < 30:
    print("🟠 Category : Overweight")
else:
    print("🔴 Category : Obesity")

print()
print("💡 Tip: Maintain a balanced diet and healthy lifestyle.")
print("=" * 45)
