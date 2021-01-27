from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self, html) -> None:
        self.soup = BeautifulSoup(html, 'html.parser')
        self.results = self.soup.find_all('li', class_='posts-listing__item')
    async def json(self): 
        for result in self.results:
            self._resultArr:list = list()
            self.title = result.find('span', class_='post-card__title')
            self.image = result.find('img', class_='lazy-image__img')
            if self.title != None and self.image != None:
                self._resultArr.append({'title': self.title.text,'image': self.image['src']})
        return self._resultArr