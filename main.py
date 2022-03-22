import logging
from src.wikipedia import WikipediaPage

URL = 'https://en.wikipedia.org/wiki/CHIP-8'


def main():
    logging.basicConfig(filename='test.log', level=logging.DEBUG)
    wikipedia_page = WikipediaPage(URL)
    text_tree = wikipedia_page.get_text_tree()
    breakpoint()


if __name__ == '__main__':
    main()
