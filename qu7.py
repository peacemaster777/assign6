# Ques 7
class Student:
    pass
class Marks:
    pass
#creating instances of classes
student1 = Student()
student2 = Student()
marks1 = Marks()
marks2 = Marks()
#checking if instances belong to respective class
print(isinstance(student1, Student))
print(isinstance(student2, Student))
print(isinstance(marks1, Marks))
print(isinstance(marks2, Marks))
#checking subclasses
print(issubclass(Student, object))
print(issubclass(Marks, object))

#output true
#true
#true
#true
#true
#true
