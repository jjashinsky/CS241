"""
File: check07b.py
Author: Br. Burton

Demonstrates abstract base classes.
"""

from abc import abstractmethod
from abc import ABC



#TODO: convert this to an ABC 
class Shape(ABC):
    def __init__(self):
        self.name = ""
    
    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))
     

    #TODO: Add an abstractmethod here called get_area
    @abstractmethod 
    def get_area(self):
        pass


#TODO: Create a Circle class here that derives from Shape
class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.radius = radius
        
    def get_area(self):
        return 3.14 * self.radius**2


#TODO: Create a Rectangle class here that derives from Shape
class Rectangle(Shape):
    
    def __init__(self, length, width):
        super().__init__()
        self.name = "Rectangle"
        self.length = length
        self.width = width
        
    def get_area(self):
        return self.length * self.width



def main():

    #TODO: Declare your list of shapes here
    my_shapes = []

    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            #TODO: Declare your Circle here, set its radius, and
            # add it to the list
            my_shapes.append(Circle(radius))
        
        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            #TODO: Declare your Rectangle here, set its length
            # and width, and add it to the list
            my_shapes.append(Rectangle(length, width))
    
    for shape in my_shapes:
        shape.display()

    # Done entering shapes, now lets print them all out:

    #TODO: Loop through each shape in the list, and call its display function


if __name__ == "__main__":
    main()
