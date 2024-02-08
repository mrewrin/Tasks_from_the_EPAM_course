# Define a base class SchoolMember representing a member of a school.
class SchoolMember:
    # Initialize the SchoolMember object with a name and age.
    def __init__(self, name: str, age: int):
        self.name = name  # Initialize the name attribute.
        self.age = age  # Initialize the age attribute.

    # Method to display the details of the school member.
    def show(self):
        return f'Name: {self.name}, Age: {self.age}'


# Define a subclass Teacher, inheriting from SchoolMember.
class Teacher(SchoolMember):
    # Initialize the Teacher object with a name, age, and salary.
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)  # Call the constructor of the parent class.
        self.salary = salary  # Initialize the salary attribute.

    # Method to display the details of the teacher, including salary.
    def show(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


# Define a subclass Student, inheriting from SchoolMember.
class Student(SchoolMember):
    # Initialize the Student object with a name, age, and grades.
    def __init__(self, name: str, age: int, grades: int):
        super().__init__(name, age)  # Call the constructor of the parent class.
        self.grades = grades  # Initialize the grades attribute.

    # Method to display the details of the student, including grades.
    def show(self):
        return f'Name: {self.name}, Age: {self.age}, Grades: {self.grades}'
