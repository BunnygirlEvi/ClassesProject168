class Bookshelf:

    def __init__(self,name,author,price,publishing_year):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_publishyear = publishing_year
        
    def add_book(self):
        print("Book Name: "+self.book_name)
        print("Author: "+self.book_author)
        print("Price: "+self.book_price)
        print("Book was published in: "+self.book_publishyear)
        print("Book Added")
    
    def years_since_published(self):
        years = 2024 - int(self.book_publishyear)
        print("Book was published " + str(years) + " years ago")
        
Book1 = Bookshelf("Harry Potter and the Philosopher's Stone", "J.K Rowling", "10.00", "1997")
Book2 = Bookshelf("Emily Windsnap and the Monster from the Deep", "Liz Kessler", "6.99", "2004")
Book1.add_book()
Book1.years_since_published()
Book2.add_book()
Book2.years_since_published()
    