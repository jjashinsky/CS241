from collections import deque

class Student:
    
    def __init__(self):
        self.name = ""
        self.course = ""
        
    def prompt(self):
        self.name = input("Enter name: ")
        self.course = input("Enter course: ")
        print()
    
    def display(self):
        print("Now helping {} with {}\n" .format(self.name, self.course))

class HelpSystem:
    
    def __init__(self):
        self.waiting_list = deque()
        
    def is_student_waiting(self):
        if len(self.waiting_list) > 0:
            return True
    
    def add_to_waiting_list(self, Student):
        self.waiting_list.append(Student)
    
    def help_next_student(self):
        if self.is_student_waiting():
            self.waiting_list.popleft().display()
        else:
            print("No one to help\n")


def main():
    
    wait_list_system = HelpSystem() 
    choice = None
    while choice != "3":
        print("Options:")
        print("1. Add a new student")
        print("2. Help next student")
        print("3. Quit")
        choice = input("Enter selection: ")
        print()
        
        if choice == "1":
            new_student = Student()
            new_student.prompt()
            wait_list_system.add_to_waiting_list(new_student)
        elif choice == "2":
            wait_list_system.help_next_student()
        elif choice == "3":
            pass
        else:
            print("Please enter a number.")
            print()
            
    print("Goodbye.")
    
     
if __name__ == "__main__":
  main()