print("книга")
class book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


    def __str__(self):
        return (f"Книга: {self.title}, автор: {self.author}, страниц: {self.pages}, год: {self.year}")



Book = book("1984", "арт", 328, 1949)
print(Book)


