class Book:
    
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0
        
    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Publication Year: ")
    
    def display_book_info(self):
        print("\n{} ({}) by {}" .format(self.title, self.publication_year, self.author))
        
        
class TextBook(Book):
    
    def __init__(self):
        super().__init__()
        self.subject = ""
        
    def prompt_subject(self):
        self.subject = input("Subject: ")
        
    def display_subject(self):
        print("Subject: {}" .format(self.subject))

class PictureBook(Book):
    
    def __init__(self):
        super().__init__()
        self.illustrator = ""
        
    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")
    
    def display_illustrator(self):
        print("Illustrated by {}" .format(self.illustrator))
    

def main():
   
   book = Book()
   book.prompt_book_info()
   book.display_book_info()
   
   print()
   
   book2 = TextBook()
   book2.prompt_book_info()
   book2.prompt_subject()
   book2.display_book_info()
   book2.display_subject()
   
   print()
   
   book3 = PictureBook()
   book3.prompt_book_info()
   book3.prompt_illustrator()
   book3.display_book_info()
   book3.display_illustrator()


if __name__ == "__main__":
    main()