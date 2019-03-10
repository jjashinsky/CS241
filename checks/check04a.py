class Person:
    
    def __init__(self):
        self.name = "anonymous"
        self.year = "unknown"
    
    def display(self):
        print("Author:\n{} (b. {})" .format(self.name, self.year))
        

class Book:
    
    def __init__(self):
        self.title = "untitled"
        self.author = Person()
        self.publisher = "unpublished"
        
    def display(self):
        print("{}" .format(self.title))
        print("Publisher:\n{}" .format(self.publisher))
        self.author.display()
        
        
def main():
    
    new_book = Book()
    
    new_book.display()
    
    print("")
    
    print("Please enter the following:")
    
    new_book.author.name = input("Name: ")
    new_book.author.year = input("Year: ")
    new_book.title = input("Title: ")
    new_book.publisher = input("Publisher: ")
    
    print("")
    
    new_book.display()
    
        
if __name__ == "__main__":
  main()
        