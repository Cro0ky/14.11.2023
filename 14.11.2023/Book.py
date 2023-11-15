class Book:
    def __init__(self, title, author, izdatel):
        self.title = title
        self.author = author
        self.izdatel = izdatel

    def get_title(self):
        print(self.title)

    def get_author(self):
        print(self.author)

    def get_izdatel(self):
        print(self.izdatel)

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_izdatel(self, izdatel):
        self.izdatel = izdatel

    def __str__(self):
        return f'\nЗаголовок - {self.title}\nАвтор - {self.author}\nИздатель - {self.izdatel}'


book = Book('title', 'author', 'izdatel')
book.get_title()
book.get_author()
book.get_izdatel()
print(book)
