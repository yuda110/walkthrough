class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def print_person(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, score):
        super().__init__(firstName, lastName, idNumber)
        self.score = score

    def calculate(self):
        av = sum(self.score)/len(self.score)
        if 90 <= av <= 100:
            grade = 'O'
        elif 80 <= av < 90:
            grade = 'E'
        elif 70 <= av < 80:
            grade = 'A'
        elif 55 <= av < 70:
            grade = 'P'
        elif 40 <= av < 55:
            grade = 'D'
        else:
            grade = 'T'
        return grade

s = Student('Dahyun', 'Yu', 8135627, [100, 80])
s.printPerson()
print("Grade:", s.calculate())