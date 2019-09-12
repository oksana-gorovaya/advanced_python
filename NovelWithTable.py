from BookErrors import *
from Novel import Novel


class NovelWithTable(Novel):

    def __init__(self, author, year, title, content=[], table={}):
        super().__init__(author, year, title)
        self.content = content
        self.table = table
        self.size = len(self.content)

    def search(self, chapter_name):
        try:
            return self.table[chapter_name]
        except:
            raise PageNotFoundError

    def add_chapter(self, chapter_name, page):
        if chapter_name in self.table.keys():
            raise Exception('Duplicate chapter')
        return self.table.update({chapter_name: page})

    def remove_chapter(self, chapter_name):
        try:
            del self.table[chapter_name]
        except:
            raise PageNotFoundError
