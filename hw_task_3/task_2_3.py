class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.knowledge = []

    def __len__(self):
        return len(self.knowledge)

    def take(self, subject):
        self.knowledge.append(subject)

    def forget(self, subject):
        self.knowledge.remove(subject)


class Teacher(Person):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.student_count = 0

    def teach(self, subject, students):
        for student in students:
            student.take(subject)
            self.student_count += 1


class StudyMaterials:
    def __init__(self, *args):
        self.materials = list(args)

    def __len__(self):
        return len(self.materials)


materials = StudyMaterials('Python', 'Version Control Systems',
                           'Relational Databases', 'NoSQL databases', 'Message Brokers')
teacher = Teacher('Мария', 'Иванова', 39, 'Женский')

# Use parentheses to create instances of Student
student1 = Student('Иван', 'Иванов', 17, 'Мужской')
student2 = Student('Петр', 'Петров', 16, 'Мужской')
student3 = Student('Елена', 'Максимова', 16, 'Женский')
student4 = Student('Максим', 'Максимов', 16, 'Мужской')
teacher.teach(materials.materials[0], [student1, student2, student3, student4])
teacher.teach(materials.materials[1], [student1, student2])
teacher.teach(materials.materials[2], [student1, student3])
teacher.teach(materials.materials[3], [student2, student3])
teacher.teach(materials.materials[4], [student1, student4])
print(student1.knowledge)
print(student2.knowledge)
print(student3.knowledge)
print(student4.knowledge)
print(len(materials))
print(len(student3))
student3.forget('Python')
print(len(student3))