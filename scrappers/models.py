import requests
from bs4 import BeautifulSoup


class Scrapper(object):
    """
    Base class to each of the scrappers used.
    @url: which page search for.
    @headers: accept language.
    @component: wich one is the HTML component that has the info.
    """

    def __init__(self, url, cinema=None):
        """
        Initialize the Soup library data.
        """
        self.url = url
        self.headers = {"Accept-Language": "en-US, en;q=0.5"}
        self.events = []
        self.soup = BeautifulSoup(self._request_url().content, "html.parser")
        self.cinema = cinema

    def _request_url(self):
        return requests.get(url=self.url, headers=self.headers)

    def _initialize(self):
        pass

    def _read_event(self):
        pass

    def _create_event(self, event):
        self.events.append(event)

    def run(self):
        return self._initialize()
