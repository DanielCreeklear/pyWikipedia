from functools import reduce
from logging import error
from time import strftime


class Text:
    def __init__(self, title: str):
        self.title = title
        self.paragraphs = []

    def insert(self, paragraph) -> None:
        self.paragraphs.append(paragraph)

    def get_tree(self):
        try:
            return {self.title: reduce(lambda a, b: a + b,
                                       [item.get_tree() for item in self.paragraphs if type(item) is Text] +
                                       [item for item in self.paragraphs if type(item) is dict or type(item) is str])}
        except TypeError:
            return {self.title: [item.get_tree() for item in self.paragraphs if type(item) is Text] +
                                [item for item in self.paragraphs if type(item) is dict or type(item) is str]}

    def __len__(self):
        return len(self.paragraphs)

    def __add__(self, otherText):
        return {self.title: self.paragraphs, otherText.title: otherText.paragraphs}
