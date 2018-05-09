class InventoryItem(object):
    def __init__(self,title, description, price, store_id):
        self.title = title
        self.description = description
        self.price = price
        self.store_id = store_id

    def __str__(self):
        return self.title

    def __eq__(self, other):
        if self.store_id == other.title:
            return True
        else:
            return False

    def change_description(self, description=""):
        if not description:
            description = input("Please give me a description: ")
        self.description = description

    def change_price(self, price= -1):
        while price < 0:
            price = input("Please give me the new price: (X.XX) :")
            try:
                price = float(price)
                break
            except:
                print("I\'m sorry but () isn't valid. " .format(price))
        self.price = price

    def change_title(self, title):
        if not title:
            title = input("Please giveme a new title: ")
        self.title = title

class Book(InventoryItem):
    def __init__(self, title, description, price, format, author, store_id):
        super(Book, self).__init__(title = title,
                                   description = description,
                                   price = price,
                                   store_id= store_id)
        self.format = format
        self.author = author

    def __str__(self):
        book_line = "{title} by {author}" .format(title = self.title, author = self.author)
        return book_line

    def _eq_(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False
    def change_format(self, format):
        if not format:
            format = input("Please give me the new format: ")
        self.format = format

    def change_author(self, author):
        if not author:
            author = input("Please give me the new author")
        self.author = author

hamlet = Book(title = "Hamlet",\
              description = "A Dane has abad time ",
              price = 5.59,
              format = "paperback",
              store_id = "123456789",
              author = "William Shakespeare")

hamlet = Book(title = "Hamlet",\
              description = "A Dane has abad time ",
              price = 10.99,
              format = "hardback",
              store_id = "987654321",
              author = "William Shakespeare")

macbeth = Book(title = "Macbeth",\
              description = "Don't listen to starnger ladies on the side of the road ",
              price = 4.99,
              format = "papperback",
              store_id = "9876114321",
              author = "William Shakespeare")

#print(hamlet == macbeth)

#print(hamlet)

#hamlet.change_description()

#print(hamlet.description)

class Software(InventoryItem):
    def __init__(self, title, description, price, os, rating, store_id):
        super(Software, self).__init__(title = title, description = description, price = price, store_id = store_id)
        self.os = os
        self.rating = rating

    def __str__(self):
        os_rating = "{os} with {rating}".format(
            os = self.os,
            rating = self.rating)
        return os_rating


    def change_os(self, os = ""):
        if not os:
            os = input("Please give me the new operating System: ")
            self.os = os
        else:
            return False

    def change_rating(self, rating = ""):
        if not rating:
            rating = input("Please enter ERSB rating (E, T, M, and so on : ")
            self.rating= rating
        else:
            return False

python = Software(title = "python",
              description = "Nice software",
              price = 4.99,
              store_id = "123",
              os = "IOS",
              rating = "A")

print(python)
python.change_os()
print(python.os)
print(python)

python.change_rating()
print(python.rating)
print(python)