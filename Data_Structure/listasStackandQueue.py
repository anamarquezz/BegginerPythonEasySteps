class list_Stack_and_Queue:
    def __init__(self):
        self.numbers = []

    def append_numbers_stack(self):  # use stack like this, append and pop
        self.numbers.append(1)
        self.numbers.append(2)
        self.numbers.append(3)
        self.numbers.append(4)
        print("\n pop like Stack")
        print(self.numbers)
        self.numbers.pop()
        print(self.numbers)

    def append_numbers_Queue(self):  # use stack like this, append and pop
        self.numbers.append(4)
        print("\n pop like Queue")
        print(self.numbers)
        self.numbers.pop(0)
        print(self.numbers)


lsq = list_Stack_and_Queue()
lsq.append_numbers_stack()
lsq.append_numbers_Queue()
