from person import Person

class Student(Person):
    def __init__(self, first_name : str, last_name : str, age : int, student_id : int):
        super().__init__(first_name, last_name, age)
        self.student_id : int = student_id
        self.grade : int = None

    def print_student(self):
        self.print_person()
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")