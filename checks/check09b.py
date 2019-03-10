class NegativeNumberError(Exception):
    
    def __init__(self, message):
        super().__init__(message)


def get_inverse(n):
    if n < 0:
        raise NegativeNumberError("The value cannot be negative")
    inverse = 1 / n
    return inverse

    

def main():
    
    try:
        number = float(input("Enter a number: "))
        result = get_inverse(number)
        print("The result is: {}" .format(result))
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except NegativeNumberError as e:
        print("Error: {}" .format(e))
        
        
if __name__ == "__main__":
  main()