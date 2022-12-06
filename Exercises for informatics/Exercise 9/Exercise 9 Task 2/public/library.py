#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie
from moviebox import MovieBox


class Library(MovieBox):

    def __init__(self):
        self.__movies = []

    def add_movie(self, movie):
        if not movie in self.__movies:
            self.__movies.append(movie)

    def get_movies(self):
        movie_dictionary = {}
        output_movies = []
        for movie in self.__movies:
            if isinstance(movie, MovieBox):
                for temporary_movie in movie.get_movies():
                    movie_dictionary[temporary_movie.get_title()] = temporary_movie
            else:
                movie_dictionary[movie.get_title()] = movie
        for key in movie_dictionary.keys():
            output_movies.append(key)
        output_movies = sorted(output_movies)
        return output_movies

    def get_total_duration(self):
        duration = 0
        for movie in self.__movies:
            duration += movie.get_duration()
        return duration


a = Movie("The Godfather", ["Brando", "Pacino"], 175)
b = Movie("The Godfather", ["Brando", "Pacino"], 175)
c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
d = MovieBox("Top Movies", [b, c])

l = Library()
l.add_movie(a)
l.add_movie(d)
print(l.get_total_duration())  # prints 413
print(l.get_movies())  # returns the three movies c, b, a (sorted and omitting the box itself)
