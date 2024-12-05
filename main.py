from student import Student
from teacher import Teacher
from logging_decorator import logging_decorator
from double_decorator import double_decorator

@double_decorator
def print_hello_world():
    print("Hello World!")

def main():
    student = Student("Jane", "Doe", 20, 12345)
    teacher = Teacher("Jack", "Doe", 40, 54321)
    
    teacher.grade_student(student)

    print_hello_world()

if __name__ == "__main__":
    main()