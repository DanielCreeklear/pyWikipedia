from requests import get


def get_link_wikipedia_by_phrase(phrase: str) -> str:
    response = get(__link_api_search(phrase)).json()
    return response[len(response)-1][0]


def __link_api_search(search: str) -> str:
    return f'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search={search}&namespace=0&limit=1'
