# -*- coding: utf-8 -*-
"""Interfaces to all of the User objects offered by the Trakt.tv API"""
from api.core import get
from api.utils import slugify

__all__ = ['User']

class User:
    """A Trakt.tv User"""
    def __init__(self, username, **kwargs):
        super().__init__()
        self.username = username
        self._history_movies = self._history_shows = self._history_episodes = None
        self._settings = None

        if len(kwargs) > 0:
            self._build(kwargs)
        else:
            self._get()

    @get
    def _get(self):
        """Get this :class:`User` from the api.tv API"""
        data = yield 'users/{username}'.format(username=slugify(self.username))
        self._build(data)

    def _build(self, data):
        """Build our this :class:`User` object"""
        for key, val in data.items():
            setattr(self, key, val)
            
    # Written by Scott Willsey
    @get
    def get_history_movies(self, start_date=None, end_date=None):
        """Watched history for all :class:`Movie`'s in this :class:`User`'s
        collection.
        """
        if self._history_movies is None:
            url = 'users/{user}/history/movies'.format(
                user=slugify(self.username)
            )
            # Check if start_date is provided and append the query parameter
            if start_date:
                url += '?start_at=' + slugify(start_date)
            
            data = yield url
            self._history_movies = []
            for movie in data:
                movie_data = movie.pop('movie')
                movie_data.update(movie)
                self._history_movies.append(movie_data)
        yield self._history_movies
        
    # Written by Scott Willsey
    @get
    def get_history_shows(self, start_date=None):
        """Watched history for all :class:`Movie`'s in this :class:`User`'s
        collection.
        """
        if self._history_shows is None:
            url = 'users/{user}/history/shows'.format(
                user=slugify(self.username)
            )
            # Check if start_date is provided and append the query parameter
            if start_date:
                url += '?start_at=' + slugify(start_date)
            
            data = yield url
            self._history_shows = []
            for show in data:
                show_data = show.pop('show')
                show_data.update(show)
                self._history_shows.append(show_data)
        yield self._history_shows
    
    # Written by Scott Willsey
    @get
    def get_history_episodes(self, start_date=None):
        """Watched history for all :class:`Movie`'s in this :class:`User`'s
        collection.
        """
        if self._history_episodes is None:
            url = 'users/{user}/history/episodes'.format(
                user=slugify(self.username)
            )
            # Check if start_date is provided and append the query parameter
            if start_date:
                url += '?start_at=' + slugify(start_date)
            
            data = yield url
            self._history_episodes = []
            for episode in data:
                episode_data = episode.pop('episode')
                episode_data.update(episode)
                self._history_episodes.append(episode_data)
        yield self._history_episodes

    def __str__(self):
        """String representation of a :class:`User`"""
        return '<User>: {}'.format(self.username)
    __repr__ = __str__
