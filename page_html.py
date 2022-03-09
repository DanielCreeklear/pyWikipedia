from logging import error
from functools import reduce
from bs4 import BeautifulSoup, PageElement
from requests import get, Response
from time import strftime


class Html:
    def __init__(self, url: str) -> None:
        self.html = RequestHtml(url).to_str()
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.soup.prettify()

    def get_all_titles_elements(self) -> dict:
        titles = self.__get_dict_title_levels(1, 7)
        for title in titles:
            for text in self.soup.find_all(title):
                titles[title].append(text)
        return titles

    def get_all_paragraph_elements(self) -> list:
        return [text for text in self.soup.find_all('p')]

    @staticmethod
    def __get_dict_title_levels(initial_level: int, final_level: int) -> dict:
        titles = {}
        for number in range(initial_level, final_level + 1):
            titles[f'h{number}'] = []
        return titles

    @staticmethod
    def get_element_tag(page_element: PageElement) -> str:
        return page_element.prettify()[page_element.prettify().find('<') + 1: page_element.prettify().find(' ')] \
            .replace('>', '').replace('\n', '')

    @staticmethod
    def this_element_has(page_element: PageElement, **kwargs) -> bool:
        try:
            return reduce(lambda a, b: a and b,
                          [page_element.get(attribute) == kwargs[attribute] for attribute in kwargs])
        except TypeError:
            return True

    def get_number_of_titles(self) -> int:
        titles = self.get_all_titles_elements()
        return reduce(lambda a, b: a + b, [len(titles[title_level]) for title_level in titles])

    def get_number_of_paragraphs(self) -> int:
        paragraphs = self.get_all_paragraph_elements()
        return len(paragraphs)

    @staticmethod
    def from_this_element_find_next(from_this_element: PageElement, tag: str, class_attr=None, **kwargs) -> PageElement:
        page_element = from_this_element
        while True:
            try:
                page_element = page_element.find_next()
                page_element_type = Html.get_element_tag(page_element)
            except AttributeError as exception:
                error(f'[{strftime("%D %H:%M:%S")}]: {exception.args}')
                return PageElement()
            else:
                if page_element_type == tag and Html.this_element_has(page_element, **kwargs) \
                        and (page_element.get('class') == class_attr or class_attr is None):
                    return page_element

    @staticmethod
    def get_elements_from_this_element_to(from_this_element: PageElement, tag: str, class_attr=None, **kwargs) -> list:
        page_element = from_this_element
        elements = []
        while True:
            try:
                page_element = page_element.find_next()
                page_element_type = Html.get_element_tag(page_element)
            except AttributeError as exception:
                error(f'[{strftime("%D %H:%M:%S")}]: {exception.args}')
                break
            else:
                elements.append(page_element)
                if page_element_type == tag and Html.this_element_has(page_element, **kwargs) \
                        and (page_element.get('class') == class_attr or class_attr is None):
                    break
        return elements


class RequestHtml:
    def __init__(self, url: str) -> None:
        self.url = url
        self.html_response = self.__get_html()

    def to_str(self) -> str:
        return self.html_response.text

    def __get_html(self) -> Response:
        try:
            page = get(self.url)
        except Exception as exception:
            error(f'[{strftime("%D %H:%M:%S")}]: {exception.args}')
            return Response()
        else:
            return page
