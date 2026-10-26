class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

bank_account = input().split(", ")
pin_code = int(bank_account[0])
balance = float(bank_account[1])
age = int(bank_account[2])

while True:
    command = input()
    if command == "End":
        break

    command = command.split("#")

    if command[0] == "Send Money":
        money = float(command[1])
        security_code = int(command[2])

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if security_code != pin_code:
            raise PINCodeError("Invalid PIN code")

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        print(f"Successfully sent {money:.2f} money to a friend")
        balance -= money
        print(f"There is {balance:.2f} money left in the bank account")

    elif command[0] == "Receive Money":
        money = float(command[1])

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        money /= 2
        balance += money

        print(f"{money:.2f} money went straight into the bank account")