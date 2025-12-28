print("=" * 40)
print("          🏦 ATM SIMULATION")
print("=" * 40)

balance = 10000.00 # Initalizing the current balance 

while True:    
    print("\nSelect an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4) : ")
    
    if choice==4:
        print("-" * 40)
        print("Thank you for using the ATM 👋")
        print("-" * 40)
        break
    if choice not in ["1","2","3"]:
        print("❌ Invalid choice. Please select between 1-4.")
        continue
    
    try:
        if choice == "1":
             print(f"💰 Your current balance is: Rs. {balance:.2f}")
             
        
        elif choice == "2":
            deposit = float(input("Enter amount to deposit: Rs. "))
            if deposit <= 0:
                print("❌ Deposit amount must be greater than zero.")
            else:
                balance += deposit
                print(f"✅ Deposit successful! New balance: Rs. {balance:.2f}")
                
        elif choice == "3":
            withdraw = float(input("Enter amount to withdraw: Rs. "))
            if withdraw <= 0:
                print("❌ Withdrawal amount must be greater than zero.")
            elif withdraw > balance:
                print("❌ Insufficient balance.")
            else:
                balance -= withdraw
                print(f"✅ Withdrawal successful! Remaining balance: Rs. {balance:.2f}")

    except ValueError:
        print("❌ Please enter a valid numeric amount.")