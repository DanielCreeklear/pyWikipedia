import logging
import sys
from src.wikipedia import WikipediaPage
from utils.json_generator import save_as_json
from utils.links_wikipedia import get_link_wikipedia_by_phrase


def main(phrase: str) -> None:
    logging.basicConfig(filename='test.log', level=logging.DEBUG)
    url = get_link_wikipedia_by_phrase(phrase)
    wikipedia_page = WikipediaPage(url)
    texts = wikipedia_page.get_text_tree()
    save_as_json(f'{wikipedia_page.get_main_title().get_text()}.json', texts)


if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        main(' '.join(args))
    else:
        print('Please, write the phrase you want to search for: python main.py [Phrase]')
