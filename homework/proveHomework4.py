from collections import deque

class Song:
    
    def __init__(self):
        self.title = deque()
        self.artist = deque()
        
    def add_at_end(self):
        self.title.append(input("Enter the title: "))
        self.artist.append(input("Enter the artist: "))
        
    def add_at_beginning(self):
        self.title.appendleft(input("Enter the title: "))
        self.artist.appendleft(input("Enter the artist: "))
        
    def display(self):
        if len(self.title) == 0:
            print("The play list is currently empty")
        else:
            print("Playing song:")
            print("{} by {}" .format(self.title[0], self.artist[0]))
            self.title.popleft()
            self.artist.popleft()


def display_options():
    print("Options:")
    print("1. Add a new song to the end of the playlist")
    print("2. Insert a new song to the beginning of the playlist")
    print("3. Play the next song")
    print("4. Quit")


def main():
    choice = None
    song_list = Song()
    
    while choice != 4:
        display_options()
        choice = int(input("Enter selection: "))
        print()
        if choice == 1:
            song_list.add_at_end()
            print()
            
        elif choice == 2:
            song_list.add_at_beginning()
            print()
        
        elif choice == 3:
            song_list.display()
            print()
            
        elif choice == 4:
            print("Goodbye")
            
            
    
if __name__ == "__main__":
  main()