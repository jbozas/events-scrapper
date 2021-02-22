import datetime

import dateutil.parser
from bs4 import BeautifulSoup
from cinemas.models import Cinema
from scrappers.models import Scrapper


class CineMunicipalScrapper(Scrapper):
    """
    Scrapper in charge of reading the CineMunicipal data.
    url: https://cineclubmunicipal.org.ar/
    """

    def __init__(self):
        super().__init__(url='https://cineclubmunicipal.org.ar/dia-por-dia-2/')
        self.cinema, _ = Cinema.objects.get_or_create(
            name='Cine Club Municipal', location='Bv. San Juan 49, Córdoba',
            url='https://cineclubmunicipal.org.ar/')

    def run(self):
        self._read_page()
        return self.events

    def _read_page(self):
        for movie in self.soup.find_all(class_='wp_theatre_event'):
            event = self._read_event(movie_data=movie)
            self._create_event(event)

    def _clean_date(self, date):
        completed = date.split()[1].split(',')[0].split('/')
        return completed[0], completed[1]

    def _parse_datetime(self, time, date):
        """
        Returns a compatible DateTimeField.
        """
        day, month = self._clean_date(date)
        year = datetime.datetime.now().year
        return dateutil.parser.parse(f'{year}/{month}/{day} {time}')

    def _read_event(self, movie_data):
        """
        Reads each movie info in the HTML and returns
        a json with the event data.
        """
        movie_data = BeautifulSoup(str(movie_data), "html.parser")
        date = movie_data.find(class_='wp_theatre_event_date').get_text()
        time = movie_data.find(class_='wp_theatre_event_time').get_text()
        return {
            'title': movie_data.find(class_='wp_theatre_event_title').get_text(),  # NOQA
            'preview': movie_data.figure.a['href'],
            'image': movie_data.figure.img['src'],
            'datetime': self._parse_datetime(time, date)
        }
