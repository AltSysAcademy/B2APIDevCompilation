# Data Model
accounts = {
    "NinoDulay18":{
        "name":"Nino Dulay",
        "balance": 10000,
        "password": "1234",
        "email": "nino@gmail.com",
        "username": "NinoDulay18"
    },
    "JohnDoe32":{
        "name":"John Doe",
        "balance": 20000,
        "password": "4321",
        "email": "john@gmail.com",
        "username": "JohnDoe32"
    }
}


def withdraw(username, withdraw_amt):
    if withdraw_amt > accounts[username]["balance"]:
        print("You have insufficient balance to withdraw")
    else:
        accounts[username]["balance"] -= withdraw_amt
        print(f"You have successfully withdrawn Php {withdraw_amt} from your bank account.")

def deposit(username, deposit_amt):
    if deposit_amt <= 0:
        print("You can not deposit negative amount of money.")
    else:
        accounts[username]["balance"] += deposit_amt
        print(f"You have successfully deposited Php {deposit_amt} to your bank account.")

def transfer_fund(username, recipient, transfer_amt):
    if recipient in accounts:
        if transfer_amt > accounts[username]["balance"]:
            print("Insufficient balance for transfer.")
        else:
            accounts[username]["balance"] -= transfer_amt
            accounts[recipient]["balance"] += transfer_amt
            print(f"Succesfully transferred Php {transfer_amt} to {recipient}.")
    else:
        print("Recipient account does not exist.")

def register(name, password, email, username, intl_bal):
    if username in accounts:
        print("Username already exists.")
    else:
        new_account = {
            username:{
                "name": name,
                "balance": intl_bal,
                "password": password,
                "email": email,
                "username": username
            }
        }
        accounts.update(new_account)

def check_bank_info(username):
    print(f"Name: {accounts[username]['name']}")
    print(f"Username: {accounts[username]['username']}")
    print(f"Password: {accounts[username]['password']}")
    print(f"Balance: {accounts[username]['balance']}")
    print(f"Email: {accounts[username]['email']}")


register("Altis Dulay", "4321", "altis@gmail.com", "AltisDulay20", 50000)
check_bank_info("AltisDulay20")
print()
withdraw("AltisDulay20", 20000)
print()
check_bank_info("AltisDulay20")
print()
transfer_fund("AltisDulay20", "NinoDulay18", 20000)
print()
check_bank_info("AltisDulay20")
print()
check_bank_info("NinoDulay18")

'''
Welcome to Bank System
1. Login
2. Register
>>> 2

Username: 
Password:
Initial Deposit:
Email:
Username:

Are you sure? (Y/N): 


Succesfully Registered, Please Log In.
----------------------------------------------

Welcome to Bank System
1. Login
2. Register

>>> 1

Username: NinoDulay18
Password: 1234

Succesfully Logged In! What do you want to do:
1. Withdraw
2. Transfer
3. Deposit
4. Log out
>>>
'''