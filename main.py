from bs4 import BeautifulSoup
import requests

class Librarian:
    def __init__(self):
        response = requests.get("https://libraryofbabel.app/random")
        print(response.url)
        self._url = response.url
        self._home = self.get_location()
        soup = BeautifulSoup(response.text, "html.parser")
        html_page = soup.find_all("pre")[1]
        self._text = str(html_page)[5:-6]

    def get_location(self):
        return self._url.split('.')

    def get_page(self):
        return self.get_location()[-1]

    def get_book(self):
        return self.get_location()[-2]
    
    def get_shelf(self):
        return self.get_location()[-3]
    
    def get_wall(self):
        return self.get_location()[-4]

if __name__ == "__main__":
    Adam = Librarian()
