class Text:
    def __init__(self, title: str):
        self.title = title
        self.paragraphs = []
        self.links = {}

    def insert_paragraph(self, paragraph) -> None:
        self.paragraphs.append(paragraph)
