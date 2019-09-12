from BookErrors import *


class Person:
    def __init__(self, name):
        self.name = name

    def read(self, book, page):
        return book.read(page)

    def write(self, book, page, text):
        return book.write(page, text)

    def set_bookmark(self, book, page):
        if book.__class__.__name__ != 'Novel':
            raise NotExistingExtensionError
        return book.set_bookmark(self, page)

    def get_bookmark(self, book):
        if book.__class__.__name__ != 'Novel':
            raise NotExistingExtensionError
        return book.get_bookmark(self)

    def del_bookmark(self, book):
        if book.__class__.__name__ != 'Novel':
            raise NotExistingExtensionError
        return book.del_bookmark(self)

