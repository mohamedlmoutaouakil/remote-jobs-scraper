import requests

class Scraper:
    def __init__(self, URL):
        self.URL = URL
        self.html_page = requests.get(self.URL)

URL = 'https://stackoverflow.com/jobs?q=Software+Developer&r=true&c=usd&mxs=Junior'
scraper = Scraper(URL)