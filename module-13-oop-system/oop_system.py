print("Welcome to Smart School Management System")

from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def display_role(self):
        pass


class Student(Person):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_student_data(self, name, age):
        self._name = name
        self._age = age

    def get_student_data(self):
        return self._name, self._age

    def display_role(self):
        print("Role: Student")


class CollegeStudent(Student):
    def __init__(self, name, age, student_id, course_name):
        super().__init__(name, age)
        self._student_id = student_id
        self._course_name = course_name

    def display_role(self):
        print("Role: College Student")

    def display_details(self):
        print("\nStudent Details")
        print("Name:", self._name)
        print("Age:", self._age)
        print("Student ID:", self._student_id)
        print("Course Name:", self._course_name)


name = input("Enter student name: ")
age = int(input("Enter student age: "))
student_id = input("Enter student ID: ")
course_name = input("Enter course name: ")


student = Student(name, age)

college_student = CollegeStudent(
    name,
    age,
    student_id,
    course_name
)


print("\nStudent Information")
print("Name:", student.get_student_data()[0])
print("Age:", student.get_student_data()[1])

college_student.display_details()


print("\nRoles")
objects = [student, college_student]

for obj in objects:
    obj.display_role()