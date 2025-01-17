class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checkedout = False
        
    def check_out(self):
        self.__is_checkedout = True
        
    def return_book(self):
        self.__is_checkedout = False
        
    def is_available(self):
        return not self.__is_checkedout

class Library:
    def __init__(self):
        self._books = []  # Changed to single underscore
        
    def add_book(self, book):
        self._books.append(book)  # Changed to single underscore
        
    def check_out_book(self, title):
        for book in self._books:  # Changed to single underscore
            if book.title == title:
                book.check_out()
                break
                
    def return_book(self, title):
        for book in self._books:  # Changed to single underscore
            if book.title == title:
                book.return_book()
                break
                
    def list_available_books(self):
        for book in self._books:  # Changed to single underscore
            if book.is_available():
                print(f"{book.title} by {book.author}")
