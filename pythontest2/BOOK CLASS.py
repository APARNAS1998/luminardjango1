#Library_name, book_name, author, pages

class Book:
    def Library(self,Library_name):
       self.Library_name=Library_name
    def Bookdetails(self,book_name,author,pages):
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printval(self):
        print(self.Library_name)
        print(self.book_name)
        print(self.author)
        print(self.pages)
b=Book()
b.Library('Elampally')
b.Bookdetails('pathumayude adu','basheer','120')
b.printval()




