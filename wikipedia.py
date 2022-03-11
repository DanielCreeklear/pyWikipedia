from functools import reduce
from time import strftime
from bs4 import PageElement
from logging import error
from page_html import Html
from models.text import Text


class WikipediaPage(Html):
    def __init__(self, html: str):
        super().__init__(html)
        self.html = html
        self.main_title = self.get_main_title()
        self.content_elements = self.__get_content_elements()
        self.texts = []

    def get_main_title(self) -> PageElement:
        try:
            return self.get_all_titles_elements()['h1'][0]
        except IndexError as exception:
            error(f'[{strftime("%D %H:%M:%S")}]: {exception.args}')

    def __get_content_elements(self) -> list:
        main_title = self.get_main_title()
        return self.get_elements_from_this_element_to(main_title, 'div', id='mw-data-after-content')

    def get_texts(self) -> None:
        i = 0
        while i < len(self.content_elements):
            element = self.content_elements[i]
            tag = self.get_element_tag(element)

            if tag == 'h2':
                text = Text(element.get_text().replace('[edit]', ''))
                j = i + 1
                while j < len(self.content_elements):
                    sub_element = self.content_elements[j]
                    sub_tag = self.get_element_tag(sub_element)

                    if sub_tag == 'h3':
                        sub_text = Text(sub_element.get_text().replace('[edit]', ''))
                        k = j + 1
                        while k < len(self.content_elements):
                            sub_sub_element = self.content_elements[k]
                            sub_sub_tag = self.get_element_tag(sub_sub_element)

                            if sub_sub_tag == 'p':
                                sub_text.insert(sub_sub_element.get_text())
                            elif sub_sub_tag == 'h3' or sub_sub_tag == 'h2':
                                text.insert(sub_text)
                                j = k - 1
                                break
                            k += 1
                    elif sub_tag == 'p':
                        text.insert(sub_element.get_text())
                    elif sub_tag == 'h2':
                        self.texts.append(text)
                        i = j - 1
                        break
                    j += 1
            i += 1
