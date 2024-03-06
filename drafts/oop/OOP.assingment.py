class Student:
    def __init__(self, student_name, student_id, major):
        self.student_name = student_name
        self.student_id = student_id
        self.major = major

    def get_student_name(self):
        return self.student_name

    def get_student_id(self):
        return self.student_id

    def get_major(self):
        return self.major


my_student = Student("Asan", "20230001", "Computer Science")


print("Student Name:", my_student.get_student_name())
print("Student ID:", my_student.get_student_id())
print("Major:", my_student.get_major())
