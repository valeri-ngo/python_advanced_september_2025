class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

def send_money(money_, curr_code, balance, actual_code_, age_, minimum_age):
    """
    A function for sending money to a friend.
    Checking if the age restriction is valid.
    Checks if the balance is enough else raises an exception.
    Checks if the PIN code is correct else raises an exception.
    """
    if age_ < minimum_age:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
    if money_ <= 0:
        raise MoneyIsNegativeError("The amount to send must be a positive number")
    if money_ <= balance:
        if actual_code_ == curr_code:
            balance -= money_
            print(f"Successfully sent {money_:.2f} money to a friend")
            print(f"There is {balance:.2f} money left in the bank account")
        else:
            raise PINCodeError("Invalid PIN code")
        return balance
    else:
        raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

def receive_money(added_money, balance):
    """
    A function for receiving salary at the end of the month.
    If statement for checking if the balance is below zero.
    Else prints how much money are added to the bank account
    """
    if added_money < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")
    else:
        balance += added_money
        print(f"{added_money:.2f} money went straight into the bank account")
        return balance

account_details = input().split(", ")
actual_code = int(account_details[0])
initial_balance = float(account_details[1])
age = int(account_details[2])
MINIMUM_AGE = 18
# User input split by a comma and a space:
# PIN code -> actual_code, bank balance -> initial_balance, current age -> age

while True:
    command = input().split("#")
    # Read commands split by "#"
    # Send Money: money_sent#code
    # Receive Money: salary (50% is being added into the bank)

    if command[0] == "End":
        break

    if command[0] == "Send Money":
        money_sent, code = float(command[1]), int(command[2])
        initial_balance = send_money(money_sent, code, initial_balance, actual_code, age, MINIMUM_AGE)

    elif command[0] == "Receive Money":
        salary = float(command[1])
        money_added = salary / 2
        initial_balance = receive_money(money_added, initial_balance)
