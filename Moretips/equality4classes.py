# with is and ==
'''
class Student:
    pass


student1 = Student()
Student2 = Student()
print(id(student1))  # diferent objects
print(id(Student2))

print(student1 is Student2)

Student3 = student1  # equal
print(id(Student3))
print(
    f"student1= {id(student1)} and student3= {id(Student3)} = {student1 is Student3}")

print(
    f"student1= {id(student1)} and student2= {id(Student2)} = {student1 is Student2}")

'''


class student1:
    def __init__(self, id):
        self.id = id
    def __eq__(self,other):
        return self.id == other.id


studen1a = student1(1)
studen1b = student1(2)
studen1c = student1(1)
studen1d = studen1a
print(id(studen1a))  # diferent objects
print(id(studen1d))
print(
    f"\n studen1a= {id(studen1a)} and studen1d= {id(studen1d)} = {studen1a is studen1d}")
