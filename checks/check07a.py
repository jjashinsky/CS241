from abc import abstractmethod
from abc import ABC

class Car(ABC):
    
    def __init__(self):
        self.name = "Unknown model"
        
    @abstractmethod    
    def get_door_specs(self):
        return "Unknown doors"
    
class Civic(Car):
    
    def __init__(self):
        self.name = "Civic"
        
    def get_door_specs(self):
        return "4 doors"
    
class Odyssey(Car):
    
    def __init__(self):
        self.name = "Odyssey"
        
    def get_door_specs(self):
        return "2 front doors, 2 sliding doors, 1 tail gate"
    
class Ferrari(Car):
    
    def __init__(self):
        self.name = "Ferrari"
        
    def get_door_specs(self):
        return "2 butterfly doors"


def attach_doors(car_type):
    print("Attaching doors to {} - {}" .format(car_type.name, car_type.get_door_specs()))


def main():
    car1 = Civic()
    car2 = Odyssey()
    car3 = Ferrari()

    attach_doors(car1)
    attach_doors(car2)
    attach_doors(car3)

if __name__ == "__main__":
    main()