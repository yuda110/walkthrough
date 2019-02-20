
class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = abs(max(self.__elements) - min(self.__elements))

d = Difference([1, 2, 5])
d.computeDifference()
print(d.maximumDifference)

