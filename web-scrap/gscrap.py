from requests import get
from bs4 import BeautifulSoup


class NextPageNotFound(Exception):
    pass


class GScrap:
    def __init__(self, query):
        self.query = f"https://google.com/search?q={query}"
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            " AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/110.0.0.0"
            " Safari/537.36"
            " Edg/110.0.1587.50",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip",
            "DNT": "1",  # Do Not Track Request Header
            "Connection": "close",
        }

    def _get_soup(self):
        request = get(self.query, headers=self._headers)
        return BeautifulSoup(request.text, "html.parser")

    def _scrap_page(self, soup):
        h3s = soup.find_all("h3")
        return filter(lambda x: x, [h3.parent.get("href", "") for h3 in h3s])

    def _goto_next_page(self, soup):
        next_page = soup.find("a", {"id": "pnnext"})
        if not next_page:
            raise NextPageNotFound
        else:
            self.query = f"https://google.com{next_page['href']}"

    def get_links(self, count=100):
        links = []
        while len(links) < count:
            soup = self._get_soup()
            links.extend(query._scrap_page(soup))
            query._goto_next_page(soup)
        return links[:count]


if __name__ == "__main__":
    query = GScrap(input("Query: "))
    for link in query.get_links(20):
        print(link)
