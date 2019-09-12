from string import ascii_lowercase as alphabet
from Book import Book
from BookErrors import *

content = [sign for sign in alphabet]


class Notebook(Book):
    def __init__(self, title, size=12, max_sign=2000, content=None):
        super().__init__(title, content)
        self.max_sign = max_sign
        self.title = title
        if content:
            self.size = len(self.content)
        else:
            self.size = size
            self.content = ['' for _ in range(self.size)]

    def read(self, page):
        if page < 0 or page >= len(content):
            raise PageNotFoundError
        return self.content[page]

    def write(self, page, text):
        if page < 0 or page >= len(content):
            raise PageNotFoundError
        elif len(text) >= self.max_sign - len(self.content[page]):
            raise TooLongTextError
        else:
            self.content[page] += text

notebook = Notebook('note', 24, 100, content)
