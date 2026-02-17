This program is a simple Bank Management System written in Python.
It allows users to:
Register a new account
Login to their account
Check account balance
Credit (deposit) money
Debit (withdraw) money
Now I will explain it clearly step-by-step 👇
🔹 1. What is this Program?
This is a menu-driven console application that simulates basic banking operations using:
Dictionary
Functions
Loops
Conditional statements
It stores user data temporarily while the program runs.

🔹 2. Data Storage
Python
Copy code
users = {}
This is a dictionary.
Structure:
Python
Copy code
users = {
    "username1": {
        "password": "1234",
        "balance": 500
    }
}
So each user has:
username
password
balance.


🔹 3. Functions Explanation
✅ 1. register()
Purpose: Create a new user account.
Steps:
Ask for username
Check if username already exists
Ask for password
Store username, password, and balance = 0
Python
Copy code
users[username] = {"password": password, "balance": 0}
Balance is initially set to 0.
✅ 2. login()
Purpose: Authenticate user.
Steps:
Ask username
Ask password
Check if:
Username exists
Password matches
If correct → returns username
If wrong → returns None
✅ 3. balance_check(username)
Purpose: Display current balance.
It fetches:
Python
Copy code
balance = users[username]["balance"]
Prints balance in 2 decimal format:
Python
Copy code
${balance:.2f}
✅ 4. credit_amount(username)
Purpose: Deposit money.
Steps:
Ask amount
Check if amount > 0
Add amount to balance
Python
Copy code
users[username]["balance"] += amount
✅ 5. debit_amount(username)
Purpose: Withdraw money.
Steps:
Ask amount
Check if amount > 0
Check if sufficient balance
Subtract from balance
Python
Copy code
users[username]["balance"] -= amount
If balance is less → prints "Insufficient balance!"


🔹 4. Main Function
Python
Copy code
def main():
This controls the full program.
It shows main menu:
Copy code

1. Register
2. Login
3. Balance Check
4. Credit Amount
5. Debit Amount
6. Exit
But actually:
Options 3, 4, 5 are handled inside login menu.
Option 6 exits program.
When user logs in successfully, it opens:
Copy code

--- User Menu ---
1. Balance Check
2. Credit Amount
3. Debit Amount
4. Logout
Logout breaks the inner loop.


🔹 5. Program Flow
Copy code

Start
   ↓
Show Main Menu
   ↓
Register or Login
   ↓
If login successful
   ↓
Show User Menu
   ↓
Perform Banking Operations
   ↓
Logout or Exit


🔹 6. Concepts Used
This program uses:
✔ Dictionary
✔ Nested Dictionary
✔ Functions
✔ While loop
✔ Nested while loop
✔ If-else conditions
✔ Input/output
✔ Float formatting
