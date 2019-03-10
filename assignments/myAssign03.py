# This is a class for the Robot that the user will be
# able to control

class Robot:
    
    # 3 charateristics of the robot class:
    # x position
    # y position
    # remaining fuel
    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel = 100
        
    # function that fires a lazer. Uses 15 fuel
    def fire(self):
        if self.fuel >= 15:
            print("Pew! Pew!")
            self.fuel -= 15
        else:
            print("Insufficient fuel to perform action")

    # function displays the fuel and position of the robot
    def status(self):
        print("({}, {}) - Fuel: {}" .format(self.x,self.y,self.fuel))

    # function that moves the position to the left by one. Uses 5 fuel.
    def left(self):
        if self.fuel >= 5:
            self.x -= 1
            self.fuel -= 5
        else:
            print("Insufficient fuel to perform action")
    
    # function that moves the position to the right by one. Uses 5 fuel.
    def right(self):
        if self.fuel >= 5:
            self.x += 1
            self.fuel -= 5
        else:
            print("Insufficient fuel to perform action")
    
    # function that moves the position up by one. Uses 5 fuel.
    # subtracts one because the grid is upside down
    def up(self):
        if self.fuel >= 5:
            self.y -= 1
            self.fuel -= 5
        else:
            print("Insufficient fuel to perform action")
    
    # function that moves the position down by one. Uses 5 fuel.
    # adds one because the grid is upside down
    def down(self):
        if self.fuel >= 5:
            self.y += 1
            self.fuel -= 5
        else:
            print("Insufficient fuel to perform action")


# main function that will collect users commands
# and will then call the class to execute that command.
def main():
    Rob = Robot()
    choice = None
    # will kick out when user enters "quit"
    while choice != "quit":
        choice = input("Enter command: ")
        if choice == "fire":
            Rob.fire()
        elif choice == "status":
            Rob.status()
        elif choice == "left":
            Rob.left()
        elif choice == "right":
            Rob.right()
        elif choice == "up":
            Rob.up()
        elif choice == "down":
            Rob.down()
    print("Goodbye.")
    
if __name__ == "__main__":
  main()