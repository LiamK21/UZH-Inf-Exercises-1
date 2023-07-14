#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):
        if isinstance(title, str) and isinstance(actors, list) and isinstance(duration, int):
            pass
        else:
            raise Warning("Title must be string, actors must be a list containing string, and duration must be a int")
        if len(title) == 0:
            raise Warning("No title listed!")
        for i in actors:
            if not isinstance(i, str):
                raise Warning("Actors have names!")
            if len(i) == 0:
                raise Warning("Actors list not complete")
        if duration < 1:
            raise Warning("Movie is too short!")
        self.__title = title
        self.__actors = actors
        self.__duration = duration

    def get_title(self):
        return self.__title

    def get_actors(self):
        return self.__actors.copy()

    def get_duration(self):
        return self.__duration

    def __eq__(self, other):
        x = self.__title == other.__title
        y = self.__actors == other.__actors
        z = self.__duration == other.__duration
        if x and y and z:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.__title, tuple(self.__actors), self.__duration))

    def __repr__(self):
        repr = f'Movie(\"{self.__title}\", {self.__actors}, {self.__duration})'
        return repr.replace("\'", "\"")


