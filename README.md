# Advanced Python Course Project

## Summary
This project demonstrates the use of decorators in Python, as well as basic object-oriented programming concepts. Below is a summary of the key concepts and components you have learned and implemented in this project.

## Project Structure
The project consists of the following files:
- `main.py`: The main entry point of the application.
- `student.py`: Defines the `Student` class.
- `teacher.py`: Defines the `Teacher` class.
- `person.py`: Defines the `Person` class, which is the base class for `Student` and `Teacher`.
- `logging_decorator.py`: Contains the `logging_decorator` function.
- `double_decorator.py`: Contains the `double_decorator` function.
- `string_check_decorator.py`: Contains the `string_check_decorator` function.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Key Concepts

### Decorators
Decorators are a powerful feature in Python that allow you to modify the behavior of a function or method. In this project, you have implemented and used the following decorators:

- **Logging Decorator (`logging_decorator`)**:
    - Logs the function name and its arguments when the function is called.
    - Defined in `logging_decorator.py`.

- **Double Decorator (`double_decorator`)**:
    - Calls the decorated function twice.
    - Defined in `double_decorator.py`.

- **String Check Decorator (`string_check_decorator`)**:
    - Checks if all arguments passed to the function are strings and prints a message if they are not.
    - Defined in `string_check_decorator.py`.

### Object-Oriented Programming
You have also implemented basic object-oriented programming concepts by defining classes and inheritance:

- **Person Class (`Person`)**:
    - Base class with attributes `first_name`, `last_name`, and `age`.
    - Defined in `person.py`.

- **Student Class (`Student`)**:
    - Inherits from `Person` and adds `student_id` and `grade` attributes.
    - Defined in `student.py`.

- **Teacher Class (`Teacher`)**:
    - Inherits from `Person` and adds `teacher_id` attribute.
    - Includes a method to grade a student.
    - Defined in `teacher.py`.

## Main Function
The main function in `main.py` demonstrates the usage of the classes and decorators:
- Creates instances of `Student` and `Teacher`.
- Grades the student using the `Teacher` class.
- Prints the student's details.
- Calls the `print_hello_world` function, which is decorated to print "Hello World!" twice and log the call.
- Calls the `add` function, which is decorated to check if arguments are strings and log the call.

## Running the Project
To run the project, execute the `main.py` file:
```bash
python main.py
```
This will demonstrate the functionality of the decorators and the object-oriented classes you have implemented.