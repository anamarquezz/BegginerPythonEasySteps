class data_structure:
    def __init__(self):
        self.mark1 = 45
        self.mark2 = 54
        self.mark3 = 88

    def suma(self):
        print(self.mark1 + self.mark2 + self.mark3)

    def sumawithmethod(self):
        marks = [45, 54, 80]
        print(sum(marks))
        print(sum(marks)/len(marks))
        print(f"update:")
        marks.append(43)
        print(sum(marks)/len(marks))
        print(type(marks))

    def list_data_structure_operations(self):
        print("\n list_data_structure_operations \n")
        markss = [23, 56, 67]
        print(markss)
        print(f"List Structure \n Suma: {sum(markss)}")  # sum
        print(f"\n len: {len(markss)}")  # size
        print(f"Add more elements: \n ")
        markss.append(10)  # add
        print(markss)
        markss.insert(2, 60)  # insert into certain position
        print(markss)
        print(f"Remove 60")  # remove 60
        markss.remove(60)
        print(markss)
        print(f"60 in markss {60 in markss}")  # 60 is in list markss?
        print(f"10 in markss {10 in markss}")  # 10 is in list markss?
        print(f"marks index [67] : {markss.index(67)}")
        print("\n LOOP MARKKS \n")
        for mark in markss:
            print(f"mark: {mark}")


dat = data_structure()

# dat.suma()
# dat.sumawithmethod()
dat.list_data_structure_operations()
