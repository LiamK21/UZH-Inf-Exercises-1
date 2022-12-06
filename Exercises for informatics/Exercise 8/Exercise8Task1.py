class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = sorted(keywords, key=len, reverse=True)
        self.__template = template

    def __clear__(self, message):
        lowercase_input = message.lower()
        for bad_word in self.__keywords:
            if lowercase_input.__contains__(bad_word):
                if len(bad_word) >= 3:
                    profanity = (len(bad_word) // 3) * self.__template
                    if not len(bad_word) % 3 == 0:
                        profanity += self.__template[: (len(bad_word) % 3)]
                    message = message.lower().replace(bad_word, profanity)
                else:
                    message = message.lower().replace(bad_word, self.__template[: (len(bad_word) % 3)])
        return message

    def filter(self, msg):
        cleared_msg = ProfanityFilter.__clear__(self, msg)
        copy = ""
        for i, v in enumerate(msg.split(" ")):
            if v.lower() in cleared_msg:
                copy += v + " "
            else:
                copy += cleared_msg.split(" ")[i] + " "
        return copy[:-1]


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard", "z"], "?#$")
    offensive_msg = "Abc defghi Mastard mastard jklmno mastard Z"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
