class Text:
    def __init__(self, title: str):
        self.title = title
        self.paragraphs = []
        self.graph = {}
        self.links = {}

    def insert(self, paragraph) -> None:
        self.paragraphs.append(paragraph)
