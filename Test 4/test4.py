class Book:
    def __init__(self,Title,Author,is_borrowed = False):
        self.Title= Title
        self.Author = Author
        self.is_borrowed = is_borrowed

    def Borrow(self):
        self.is_borrowed=True
        print("Book is borrowed!")

    def Return_Book(self):
        self.is_borrowed=False
        print("Book is returned!")

objbook1 = Book("Cosmic","Frank Cottrell Boyce")
objbook1.Borrow()
objbook1.Return_Book()

objbook2 = Book("Global","Andrew Donkin")
objbook2.Borrow()
objbook2.Return_Book()

objbook3 = Book("Running Wild","Michael Morpurgo")
objbook3.Borrow()
objbook3.Return_Book()