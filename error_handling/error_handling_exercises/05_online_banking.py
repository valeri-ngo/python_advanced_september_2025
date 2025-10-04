class MoneyNotEnoughError(Exception):
    """Raised when there in not enough money in the bank"""
    pass

class PINCodeError(Exception):
    """Raised when PIN code is incorrect"""
    pass

class UnderageTransactionError(Exception):
    """Raised when the user is underage for the transaction"""
    pass

class MoneyIsNegativeError(Exception):
    """Raised when the transaction is negative value"""
    pass

def send_money(money_, curr_code, balance, actual_code_, age_, minimum_age):
    """
    A function for sending money to a friend.
    """
    if age_ < minimum_age:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
    # Checks if the user is underage
    if money_ <= 0:
        raise MoneyIsNegativeError("The amount to send must be a positive number")
    # Checks if the transaction is negative
    if money_ <= balance:
        # Checks if the money is enough to be sent
        if actual_code_ == curr_code:
            # Checks if the PIN code is correct
            balance -= money_
            print(f"Successfully sent {money_:.2f} money to a friend")
            print(f"There is {balance:.2f} money left in the bank account")
        #     Prints the output when everything passes True
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
        # Checks if the transaction amount is negative.
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
# User input split by a '. ':
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
