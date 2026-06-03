from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import words

WORDSET = set(words.words())

class Librarian:
    def __init__(self):
        response = requests.get("https://libraryofbabel.app/random")
        self._url = response.url
        self._home = self.get_location()
        soup = BeautifulSoup(response.text, "html.parser")
        html_page = soup.find_all("pre")[1]
        self._text = str(html_page)[5:-6]

    def _set_url(self, new_url: str) -> None:
        self._url = new_url

    def get_text(self) -> str:
        return self._text

    def get_location(self) -> list[str]:
        return self._url.split('.')

    def get_page(self) -> int:
        return int(self.get_location()[-1])

    def get_book(self) -> int:
        return int(self.get_location()[-2])
    
    def get_shelf(self) -> int:
        return int(self.get_location()[-3])
    
    def get_wall(self) -> int:
        return int(self.get_location()[-4])

if __name__ == "__main__":
    Adam = Librarian()
    print(Adam.get_text())
    if 'apple' in WORDSET:
        print("Huzzah!")
    else:
        print("BOOOOO!")
