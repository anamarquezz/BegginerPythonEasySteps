class Student:
    def __init__(self):
        self.marks = [5, 10, 15]

    def get_number_of_marks(self):
        return len(self.marks)

    def get_total_sum_of_marks(self):
        print(f"Suma:", sum(self.marks))

    def determine_maximum_mark(self):
        print(f"Maxime: {max(self.marks)}")

    def determine_minimum_mark(self):
        print(f"Minimum: {min(self.marks)}")

    def determine_average(self):
        print(f"Average: {sum(self.marks) / len(self.marks)}")

    def add_new_mark(self, num):
        self.marks.append(num)
        for mark in self.marks:
            print(f"mark: {mark}")

    def remove_mark_at_index(self, index):
        self.marks.remove(index)
        for mark in self.marks:
            print(f"mark: {mark}")


exercises = Student()
print(f"\n Number of marks: {exercises.get_number_of_marks()}")
print("\n")
exercises.get_total_sum_of_marks()
print("\n")
exercises.determine_maximum_mark()
print("\n")
exercises.determine_minimum_mark()
print("\n")
exercises.determine_average()
print("\n")
exercises.add_new_mark(20)
print("\n")
exercises.remove_mark_at_index(20)
