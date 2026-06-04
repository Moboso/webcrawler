from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import words

WORDSET = {word.lower() for word in words.words()}

class Librarian:
    def __init__(self):
        self._response = requests.get("https://libraryofbabel.app/random")
        self.home = self.location

    @property
    def url(self):
        return self._response.url

    @property
    def text(self) -> str:
        soup = BeautifulSoup(self._response.text, "html.parser")
        html_text = soup.find_all("pre")[1] # Get the page text as a Tag
        return str(html_text)[5:-6] # Convert the text into a string
    
    @property
    def location(self) -> list[str]:
        return self.url.split('.')

    @property
    def page(self) -> int:
        return int(self.location[-1])

    @property
    def book(self) -> int:
        return int(self.location[-2])
    
    @property
    def shelf(self) -> int:
        return int(self.location[-3])
    
    @property
    def wall(self) -> int:
        return int(self.location[-4])

if __name__ == "__main__":
    Adam = Librarian()
    print(Adam.home)
    if 'aple'.lower() in WORDSET:
        print("Huzzah!")
    else:
        print("BOOOOO!")
