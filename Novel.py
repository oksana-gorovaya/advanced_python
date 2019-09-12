from Book import Book
from string import ascii_lowercase as alphabet
from BookErrors import *
from Person import Person
content = [sign for sign in alphabet]


class Novel(Book):
    def __init__(self, author, year, title, content=None):
        super().__init__(title, content)
        self.author = author
        self.year = year
        self.bookmark = {}

    def read(self, page):
        if page < 0 or page >= len(content):
            raise PageNotFoundError
        return self.content[page]

    def set_bookmark(self, person, page):
        if page < 0 or page >= len(content):
            raise PageNotFoundError
        if isinstance(person, Person):
            self.bookmark.update({person.__hash__(): page})

    def get_bookmark(self, person):
        if self.bookmark.get(person.__hash__()) is None:
            raise PageNotFoundError
        return self.bookmark[person.__hash__()]

    def del_bookmark(self, person):
        if self.bookmark[person.__hash__()]:
            del self.bookmark[person.__hash__()]
        else:
            raise PageNotFoundError

    def write(self, page, text):
        raise PermissionDeniedError

