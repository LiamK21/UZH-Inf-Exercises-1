#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie


class MovieBox(Movie):

    def __init__(self, title, movies):
        if not isinstance(title, str) or not isinstance(movies, list):
            raise Warning("Input type incorrect!")
        for movie in movies:
            if not isinstance(movie, Movie):
                raise Warning("Movies list incorrect")
        self.__title = title
        self.__movies = movies

    def get_title(self):
        return self.__title

    def get_actors(self):
        actors = []
        # Loop over all movies contained in the box and return the authors
        for movie in self.__movies:
            actors.extend(movie.get_actors())
        actors = sorted(set(actors))  # Sort the authors alphabetically and remove duplicates
        return actors

    def get_duration(self):
        duration = 0
        for movie in self.__movies:
            duration += movie.get_duration()
        return duration

    def get_movies(self):
        return self.__movies.copy()

    def __hash__(self):
        return hash((self.__title, self.__movies))

    def __eq__(self, other):
        if self.get_title() == other.get_title() and self.get_movies() == other.get_movies():
            return True
        else:
            return False

    def __repr__(self):
        return f"MovieBox(\"{self.__title}\", {self.__movies})"
