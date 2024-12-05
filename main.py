from student import Student
from teacher import Teacher
from logging_decorator import logging_decorator
from double_decorator import double_decorator
from string_check_decorator import string_check_decorator

@double_decorator
@logging_decorator
def print_hello_world() -> None:
    print("Hello World!")

@logging_decorator
@string_check_decorator
def add(a : int, b : int) -> int:
    return a + b




def main():
    student = Student(first_name="Jane", last_name="Doe", age=20, student_id=12345)
    teacher = Teacher("Jack", "Off", 420, 54321)
    
    teacher.grade_student(student)

    student.print_student()

    print_hello_world()
    
    add(1, 2)

if __name__ == "__main__":
    main()