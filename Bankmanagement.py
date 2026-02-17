users = {}

def register():
    print("\n--- Registration ---")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Try a different one.")
        return
    password = input("Enter a password: ")
    users[username] = {"password": password, "balance": 0}
    print("Registration successful!")

def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password!")
        return None

def balance_check(username):
    print(f"\n--- Balance Check for {username} ---")
    balance = users[username]["balance"]
    print(f"Your current balance is: ${balance:.2f}")

def credit_amount(username):
    print(f"\n--- Credit Amount for {username} ---")
    amount = float(input("Enter the amount to credit: "))
    if amount <= 0:
        print("Invalid amount! Must be greater than zero.")
        return
    users[username]["balance"] += amount
    print(f"${amount:.2f} credited successfully!")

def debit_amount(username):
    print(f"\n--- Debit Amount for {username} ---")
    amount = float(input("Enter the amount to debit: "))
    if amount <= 0:
        print("Invalid amount! Must be greater than zero.")
        return
    if amount > users[username]["balance"]:
        print("Insufficient balance!")
        return
    users[username]["balance"] -= amount
    print(f"${amount:.2f} debited successfully!")

def main():
    while True:
        print("\n--- Bank Management System ---")
        print("1. Register")
        print("2. Login")
        print("3. Balance Check")
        print("4. Credit Amount")
        print("5. Debit Amount")
        print("6. Exit")
       
        choice = input("Choose an option: ")
        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. Balance Check")
                    print("2. Credit Amount")
                    print("3. Debit Amount")
                    print("4. Logout")
                   
                    user_choice = input("Choose an option: ")
                    if user_choice == '1':
                        balance_check(user)
                    elif user_choice == '2':
                        credit_amount(user)
                    elif user_choice == '3':
                        debit_amount(user)
                    elif user_choice == '4':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice! Please try again.")
        elif choice == '6':
            print("Account not found")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


