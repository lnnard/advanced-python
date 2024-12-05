from student import Student
from teacher import Teacher


def main():
    student = Student("Jane", "Doe", 20, 12345)
    teacher = Teacher("Jack", "Doe", 40, 54321)

    teacher.grade_student(student)

    student.print_student()




if __name__ == "__main__":
    main()