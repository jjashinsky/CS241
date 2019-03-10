class CheckingAccount:
    
    def __init__(self, starting_balance, num_checks):
        self.balance = starting_balance
        if self.balance < 0:
            raise BalanceError("Cannot have negative balance")
        
        self.check_count = num_checks
        if self.check_count < 0:
            raise OutOfChecksError("Cannot have negative checks")

    def deposit(self, amount):
        self.balance += amount
    
    def write_check(self, amount):
        if self.check_count == 0:
            raise OutOfChecksError("No checks left")
        if amount > self.balance:
            raise BalanceError("Insifficient funds")
        self.balance -= amount
        self.check_count -= 1
        
    def display(self):
        print("Current balance: {}" .format(self.balance))
        print("Number of checks left: {}" .format(self.check_count))
    
    def apply_for_credit(self, amount):
        pass
    
    def buy_checks(self):
        self.balance -= 5
        self.check_count += 25

class BalanceError(Exception):
    
    def __init__(self, message):
        super().__init__(message)
        
        
class OutOfChecksError(Exception):
    
    def __init__(self, message):
        super().__init__(message)


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            try:
                balance = float(input("Starting balance: "))
                num_checks = int(input("Numbers of checks: "))
                acc = CheckingAccount(balance, num_checks)
            except BalanceError as e:
                print("Error: {}" .format(e))
            except OutOfChecksError as e:
                print("Error: {}" .format(e))
                
        elif command == "display":
            acc.display()
            
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
            
        elif command == "check":
            try:
                amount = float(input("Amount: "))
                acc.write_check(amount)
            except OutOfChecksError as e:
                answer = None
                answer = input("You are out of checks.\nDo you want buy more? (y/n): ")
                if answer == "y":
                    acc.buy_checks()
                    print("You bought 25 more checks for $5")
                    print("You may now try writing another check")
            except BalanceError as e:
                print("Error: {}" .format(e))
            
        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)


if __name__ == "__main__":
    main()
    