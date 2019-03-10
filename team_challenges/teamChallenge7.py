class Employee:
    
    def __init__(self):
        self.name = "Employee"
        
    @abstractmethod
    def display_name(self):
        print("{}" .format(self.name))
        
    def prompt_name(self):
        self.name = input("\nName: ")
    
    
class HourlyEmployee(Employee):
    
    def __init__(self):
        super().__init__()
        self.hourly_wage = 0
    
    def prompt_hourly_wage(self):
        self.hourly_wage = input("Enter hourly wage: ")
    
    def display(self):
        print("{} - ${}/hour" .format(self.name, self.hourly_wage))
        
class SalaryEmployee(Employee):
    
    def __init__(self):
        super().__init__()
        self.salary = 0
        
    def prompt_salary(self):
        self.hourly_wage = input("Enter salary: ")
        
    def display(self):
        print("{} - ${}/year" .format(self.name, self.salary))
        
def main():
    
    list_of_dudes = []
    choice = None
    
    while choice != "q":
        choice = input("Enter command: ")
        if choice == "h":
            dude = HourlyEmployee()
            dude.prompt_name()
            dude.prompt_hourly_wage()
            print()
            
            list_of_dudes.append(dude)
            
            
        elif choice == "s":
            dude = SalaryEmployee()
            dude.prompt_name()
            dude.prompt_salary()
            print()
            
            list_of_dudes.append(dude)
            
    for dude in list_of_dudes:
        print()
        dude.display()
        
    print("\nGoodbye.")
    
    
if __name__ == "__main__":
    main()