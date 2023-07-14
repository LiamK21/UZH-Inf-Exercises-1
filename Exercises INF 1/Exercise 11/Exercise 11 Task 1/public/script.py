#!/usr/bin/python3
import string

from data import words


def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]


def words_containing_string(s):
    return [i for i in words if i.__contains__(s)]


def words_starting_with_character(c):
    return [word for word in words if word[0] == c]


def alphabet():
    '''you don't have to solve this one using a comprehension.'''
    return string.ascii_lowercase


def dictionary():
    return {char: words_starting_with_character(char) for char in alphabet()}


def censored_words(s):
    return ["x" * len(word) if word.__contains__(s) else word for word in words]

print(censored_words("cable"))