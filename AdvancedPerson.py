from pyparsing import basestring
from Person import Person
from BookErrors import *


class AdvancedPerson(Person):
    def __init__(self, name):
        super().__init__(name)

    def search(self, book, chapter_name):
        return book.search(chapter_name)

    def read(self, book, search_term):
        if isinstance(search_term, basestring):
            return book.search(search_term)
        elif isinstance(search_term, int):
            chapter_found = []
            for key, value in book.table.items():
                if search_term == value:
                    chapter_found.append(key)
            if len(chapter_found) > 0:
                return ', '.join(chapter_found)
            else:
                raise PageNotFoundError
        else:
            raise Exception('Invalid search term')

    def write(self, book, chapter_name, page):
        return book.add_chapter(chapter_name, page)
