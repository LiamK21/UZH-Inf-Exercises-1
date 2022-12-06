class Publication:

    def __init__(self, authors, title, year):
        self.__authors = str(authors).replace("\'", "\"")
        self.__title = title
        self.__year = year

    def get_authors(self):
        return self.__authors

    def get_title(self):
        title = self.__title[:]
        return title

    def get_year(self):
        year = self.__year
        return year

    def __str__(self):
       return f"Publication({self.__authors}, \"{self.__title}\", {self.__year})"

    def __repr__(self):
        return f"Publication({self.__authors}, \"{self.__title}\", {self.__year})"

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        x = self.__authors == other.__authors
        y = self.__title == other.__title
        z = self.__year == other.__year
        if x and y and z:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.__authors, self.__title, self.__year))

    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if not self.__authors == other.__authors:
            return self.__authors > other.__authors
        if not self.__title == other.__title:
            return self.__title > other.__title
        if not self.__year == other.__year:
            return self.__year > other.__year
        return False

    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if not self.__authors == other.__authors:
            return self.__authors >= other.__authors
        if not self.__title == other.__title:
            return self.__title >= other.__title
        if not self.__year == other.__year:
            return self.__year >= other.__year
        return False

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if not self.__authors == other.__authors:
            return self.__authors <= other.__authors
        if not self.__title == other.__title:
            return self.__title <= other.__title
        if not self.__year == other.__year:
            return self.__year <= other.__year
        return False

    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if not self.__authors == other.__authors:
            return self.__authors < other.__authors
        if not self.__title == other.__title:
            return self.__title < other.__title
        if not self.__year == other.__year:
            return self.__year < other.__year
        return False


if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    sales = {
        p1: 273,
        p2: 398,
    }
pp = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
print(pp.get_authors())