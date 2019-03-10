def main():
    even = []
    odd = []
    choice = None
    while choice != 0:
        choice = int(input("Enter a number (0 to quit): "))
        if choice % 2 == 0:
            even.append(choice)
        elif choice % 2 != 0:
            odd.append(choice)
            
    print()
            
    print("Even numbers:")
    for i in range(len(even)-1):
        print(even[i])
    
    print()
    
    print("Odd numbers:")
    for i in range(len(odd)):
        print(odd[i])
    
if __name__ == "__main__":
  main()