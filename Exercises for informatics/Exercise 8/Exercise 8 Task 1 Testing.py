from unittest import TestCase
from Exercise8Task1 import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    def test_example_more_than_1(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno batch"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno ?#$?#"
        self.assertEqual(expected, actual)

    def test_example_after_each_other(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc duckshot mastard der"
        actual = f.filter(msg)
        expected = "abc ?#$??#$? ?#$?#$? der"
        self.assertEqual(expected, actual)

    def test_no_filter(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi hello jklmno"
        actual = f.filter(msg)
        expected = "abc defghi hello jklmno"
        self.assertEqual(expected, actual)

    def test_substring(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno mabatchff"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno ma?#$?#ff"
        self.assertEqual(expected, actual)

    def test_2_in_1(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno myduckgotshotonce"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno my?#$?got?#$?once"
        self.assertEqual(expected, actual)

    def test_smaller_string(self):
        f = ProfanityFilter(["a", "b", "c", "d", "abc"], "?#$")
        msg = "abc a b c d defgha"
        actual = f.filter(msg)
        expected = "?#$ ? ? ? ? ?efgh?"
        self.assertEqual(expected, actual)

    def test_smaller_string_upper_and_lower(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "ShOt defghi mastard JKLMNO"
        actual = f.filter(msg)
        expected = "?#$? defghi ?#$?#$? JKLMNO"
        self.assertEqual(expected, actual)

    def test_smaller_string_uppercase(self):
        f = ProfanityFilter(["abc"], "?#$")
        msg = "abc def ABC DEF"
        actual = f.filter(msg)
        expected = "?#$ def ?#$ DEF"
        self.assertEqual(expected, actual)