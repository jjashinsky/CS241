def main():
    
    success = False
    
    while not success:
        try:
            number = int(input("Enter a number: "))
            result = number * 2
            print("The result is: {}" .format(result))
            success = True
        except ValueError:
            print("The value entered is not valid")
        
        
if __name__ == "__main__":
  main()
        