import random
from person import Person

class Teacher(Person):
    def __init__(self, first_name : str, last_name : str, age : int, teacher_id : int):
        super().__init__(first_name, last_name, age)
        self.teacher_id = teacher_id

    def print_teacher(self):
        self.print_person()
        print(f"Teacher ID: {self.teacher_id}")

    def grade_student(self, student):
        student.grade = random.randint(1, 10)