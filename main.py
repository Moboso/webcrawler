from bs4 import BeautifulSoup
import requests

class Librarian:
    def __init__(self):
        response = requests.get("https://libraryofbabel.app/random")
        print(response.url)
        self._home = response.url.split('.')
        self._location = self._home
        # soup = BeautifulSoup(response.text, "html.parser")

    def get_page(self):
        return self._location[-1]

    def get_book(self):
        return self._location[-2]
    
    def get_shelf(self):
        return self._location[-3]
    
    def get_wall(self):
        return self._location[-4]
    
    def get_hex(self):
        return self._location[-5].split('/')[-1]


if __name__ == "__main__":
    Adam = Librarian()
    print(Adam.get_hex())
