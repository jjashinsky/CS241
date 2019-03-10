class rational:
    
    def __init__(self):
        self.N = 0
        self.D = 1
        
    def prompt(self): 
        self.N = input("Enter the numerator: ")
        self.D = input("Enter the denominator: ")
        

    def display(self):
        print("{}/{}" .format(self.N, self.D))
        
    def display_decimal(self):
        print("{}" .format(float(self.N) / float(self.D)))


def main():

    r1 = rational()

    r1.display()

    r1.prompt()

    r1.display()
    
    r1.display_decimal()


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()