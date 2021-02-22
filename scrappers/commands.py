from events.models import Event
from movies.models import Movie
from scrappers.services.cineclub_municipal import CineMunicipalScrapper


class Command(object):
    """
    Command in charge of the excecution and data retrieve
    of all Scrappers in 'self.scrappers'.
    It reads the data and tries to create a new Event,
    in case it doesn't exist already.
    """

    def __init__(self):
        self.scrappers = [CineMunicipalScrapper]
        self.events = []

    def _already_exists_event(self, event, movie, cinema) -> bool:
        """
        Checks if an event already exists in the database.
        """
        return Event.objects.filter(
            movie=movie.id, cinema=cinema.id, datetime=event['datetime']
        ).exists()

    def _get_movie(self, event) -> object:
        title = event['title']
        if Movie.objects.filter(title=title).exists():
            return Movie.objects.get(title=title)
        data = {
            'preview': event.get('preview', None),
            'image': event.get('image', None),
            'title': title
        }
        return Movie.objects.create(**data)

    def _create_event(self, event, movie, cinema) -> object:
        data = {
            'datetime': event['datetime'],
            'movie': movie,
            'cinema': cinema,
        }
        return Event.objects.create(**data)

    def run(self):
        for scrapper in self.scrappers:
            events = scrapper().run()
            cinema = scrapper().cinema
            for event in events:
                movie = self._get_movie(event)
                if not self._already_exists_event(event, movie, cinema):
                    self._create_event(event, movie, cinema)
