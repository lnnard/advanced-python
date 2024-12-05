class Person:
    def __init__(self, first_name : str, last_name : str, age : int):
        self.first_name : str = first_name
        self.last_name : str = last_name
        self.age : str = age

    def print_person(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")