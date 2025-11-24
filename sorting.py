class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

students = [
    Student(3, "Riya"),
    Student(1, "Arjun"),
    Student(2, "Kabir"),
]

students.sort(key=lambda x: x.roll)

for s in students:
    print(s.roll, s.name)
