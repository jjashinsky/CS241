class student:
    
    def __init__(self):
        self.L = ""
        self.F = ""
        self.ID = 0
        
def prompt_student():
    # needed to look at checkpoint solution to understand that the
    # class can be called to create an object then editted here. 
    new_student = student()
    new_student.F = input("Please enter your first name: ")
    new_student.L = input("Please enter your last name: ")
    new_student.ID = input("Please enter your id number: ")
    return(new_student)
        

def display_student(new_student):
    print("\nYour information:")
    print("{} - {} {}" .format(new_student.ID, new_student.F, new_student.L))
    

    
def main():
     new_student = prompt_student()
     display_student(new_student)


if __name__ == "__main__":
  main()