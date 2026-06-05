# Uncomment the following lines if the 'words' corpus is not downloaded:
# import nltk
# nltk.download("words")

from bs4 import BeautifulSoup
import requests
from nltk.stem import PorterStemmer
from nltk.corpus import words

WORDSET = {word.lower() for word in words.words()}
PUNCTUATION_MARKS = ['!', '?', '.']

class Librarian:
    def __init__(self, url: str):
        self.url = url
        self._response = requests.get(self.url)
        self.home = self.url
        self.important_pages = {}
        self._stemmer = PorterStemmer()

    # def check_book(self):
    #     self._response = requests.get('.'.join(self.location[:-1] ))

    def check_page(self):
        final_words = []
        words = self.text.split()
        normalised_words = [word for word in words if len(word) >= 3 and not any(punctuation in word[:-1] for punctuation in PUNCTUATION_MARKS)]
        for word in normalised_words:
            if word in WORDSET or self._stemmer.stem(word) in WORDSET:
                final_words.append(word)
        if final_words:
            self.important_pages[self.url] = final_words
        print(self.important_pages)

    # @property
    # def url(self):
    #     return self._response.url

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
    
    @property
    def room(self):
        return self.location[-5].split('/')[-1]

if __name__ == "__main__":
    # https://libraryofbabel.app/random
    Adam = Librarian("https://libraryofbabel.app/ref/@aef2b752f39166ee61c24cf87e470820a01980b7565102ed0efe49b122492e56.1.3.29.370")
    Adam.check_page()

    # if 'dog' in WORDSET:
    #     print('yay')
    # else:
    #     print('nay')

    # foo = [0, 1, 2, 3, 4, 5]
    # bar = []
    # for num in foo:
    #     if num in [1, 2, 3]:
    #         bar.append(num)
    # for num in bar:
    #     foo.remove(num)
    # print(foo)
    # print(bar)
