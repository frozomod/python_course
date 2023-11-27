class Student:
    def __init__(self, knowledge):
        self.knowledge = knowledge

    def take(self, subject):
        self.knowledge.append(subject)


class Teacher:
    def __init__(self, student_count):
        self.student_count = student_count

    def teach(self, subject, students):
        for student in students:
            student.take(subject)
            self.student_count += 1


class StudyMaterials:
    def __init__(self, *args):
        self.materials = list(args)


materials = StudyMaterials('Python', 'Version Control Systems',
                           'Relational Databases', 'NoSQL databases', 'Message Brokers')
teacher = Teacher(student_count=0)

# Use parentheses to create instances of Student
student1 = Student(knowledge=[])
student2 = Student(knowledge=[])
student3 = Student(knowledge=[])
student4 = Student(knowledge=[])
teacher.teach(materials.materials[0], [student1, student2, student3, student4])
teacher.teach(materials.materials[1], [student1, student2])
teacher.teach(materials.materials[2], [student1, student3])
teacher.teach(materials.materials[3], [student2, student3])
teacher.teach(materials.materials[4], [student1, student4])
print(student1.knowledge)
print(student2.knowledge)
print(student3.knowledge)
print(student4.knowledge)
