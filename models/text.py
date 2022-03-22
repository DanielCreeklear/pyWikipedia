from functools import reduce
from logging import error
from time import strftime


class Text:
    def __init__(self, title: str):
        self.title = title
        self.paragraphs = []

    def insert(self, paragraph) -> None:
        self.paragraphs.append(paragraph.replace('\n', ''))

    def get_tree(self):
        try:
            return {self.title: reduce(lambda a, b: a + b,
                                       [item.get_tree() for item in self.paragraphs if type(item) is Text] +
                                       [item for item in self.paragraphs if type(item) is dict or type(item) is str])}
        except TypeError:
            return {self.title: [item.get_tree() for item in self.paragraphs if type(item) is Text] +
                                [item for item in self.paragraphs if type(item) is dict or type(item) is str]}

    def replace(self, __old, __new):
        for i in range(len(self.paragraphs)):
            self.paragraphs[i].replace(__old, __new)
        return self

    def __len__(self):
        return len(self.paragraphs)

    def __add__(self, other_text):
        return {self.title: self.paragraphs, other_text.title: other_text.paragraphs}
