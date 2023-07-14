class Fridge:
    def __init__(self):
        self.__stored_item = []
        self.__index = -1

    def __len__(self):
        return len(self.__stored_item)

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index < len(self.__stored_item):
            return self.__stored_item[self.__index]
        self.iterations = -1
        raise StopIteration

    def store(self, items):
        self.__items = items
        self.__stored_item.append(self.__items)
        self.__stored_item.sort()

    def take(self, relevant_item):
        if self.__stored_item.__contains__(relevant_item):
            self.__stored_item.remove(relevant_item)
            return relevant_item
        raise Warning("No matching Item in the fridge")

    def find(self, grocery):
        self.__grocery = grocery
        for item in self.__stored_item:
            if item[1] == grocery:
                return item
            return None

    def take_before(self, expiration_date):
        self.__expiration_date = expiration_date
        expired_groceries = []
        for i in self.__stored_item:
            if i[0] < expiration_date:
                expired_groceries.append(i)
        for expired in expired_groceries:
            self.__stored_item.remove(expired)
        return expired_groceries


f = Fridge()
f.store((191127, "Butter"))
f.store((191117, "Milk"))
f.store((191122, "Butter"))
f.store((191017, "Milk"))
f.store((220717, "frozen broccoli"))
f.store((221117, "frozen peas"))

print("Items in the fridge:")
for i in f:
    print("- {} ({})".format(i[1], i[0]))

#print(f.take((191127, "Butter")))
# f.take((191207, "Bread"))

#print("Items in the fridge:")
#for j in f:
#    print("- {} ({})".format(j[1], j[0]))

#print(f.find("Milk"))
#print(f.take_before(220101))
#
#print("Items in the fridge:")
#for a in f:
#    print("- {} ({})".format(a[1], a[0]))