from selenium import webdriver
from time import sleep

class Fetcher:
    def __init__(self, url) -> None:
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('window-size=1200x600')
        self.options.add_argument("no-sandbox")
        self.options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(chrome_options=self.options)
    async def html(self):
        self.driver.get(self.url)
        SCROLL_PAUSE_TIME = 0.5
        self.i = 0
        self.last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(SCROLL_PAUSE_TIME)
            self.new_height = self.driver.execute_script("return document.body.scrollHeight")
            if self.urlnew_height == self.last_height:
                break
            self.last_height = self.new_height
            self.i += 1
            if self.i == 5:
                break           
        sleep(5)
        self.content = await self.driver.page_source
        self.driver.quit()
        return self.content