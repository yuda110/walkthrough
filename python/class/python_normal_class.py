
class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def print_person(self):
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.id_number)


class Student(Person):
    def __init__(self, first_name, last_name, id_number, score):
        super().__init__(first_name, last_name, id_number)
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
s.print_person()
print("Grade:", s.calculate())
