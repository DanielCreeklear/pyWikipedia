import logging
from page_html import Html, RequestHtml
from wikipedia import WikipediaPage

URL = 'https://en.wikipedia.org/wiki/CHIP-8'


def main():
    logging.basicConfig(filename='test.log', level=logging.DEBUG)
    wikipedia_page = WikipediaPage(URL)
    wikipedia_page.get_texts()
    print(wikipedia_page.get_text_tree())


if __name__ == '__main__':
    main()
