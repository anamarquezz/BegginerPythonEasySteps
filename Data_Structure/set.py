from operator import attrgetter


class list_set:
    def __init__(self):
        self.numbers = [1, 2, 3, 2, 1]

    def set_op(self):
        print(self.numbers)
        # remove duplicates
        number_set = set(self.numbers)
        print(f"\n  number_set = set(self.numbers) => {number_set}")
        number_set.add(3)
        print(f"\n  number_set.add(3) => {number_set}")
        number_set.add(4)
        print(f"\n  number_set.add(4) => {number_set}")
        number_set.add(0)
        print(f"\n  number_set.add(0) => {number_set}")
        number_set.remove(0)
        print(f"\n  number_set.remove(0) => {number_set}")

        print(f"\n  number_set[0] => 'set' object does not support indexing ")

        print(f"\n\n  1 in number_set {number_set}  => {1 in number_set}")
        print(f"\n  5 in number_set {number_set} => {5 in number_set}")

        print(f"\n\n  min(number_set) {number_set} => {min(number_set)}")
        print(f"\n  max(number_set) {number_set} => {max(number_set)}")
        print(f"\n  sum(number_set) {number_set} => {sum(number_set)}")
        print(f"\n  len(number_set) {number_set} => {len(number_set)}")

        print(f"\n\n  set(range(1,6)) => {set(range(1,6))}")
        print(f"\n  set(range(4,10)) => {set(range(4,11))}")
        print(f"\n  set(range(1,6)) + set(range(4,10))  => unsupported operand type(s) for +: 'set' and 'set'")
        print(
            f"\n  set(range(1,6)) | set(range(4,10))  UNION  {set(range(1,6))} | {set(range(4,10))}  => {set(range(1,6)) | set(range(4,10))}")
        print(
            f"\n  set(range(1,6)) & set(range(4,10))  INTERSECTION  {set(range(1,6))} & {set(range(4,10))}  => {set(range(1,6)) & set(range(4,10))}")

        print(
            f"\n  set(range(1,6)) - set(range(4,10))  NOT IN  {set(range(1,6))} - {set(range(4,10))}  => {set(range(1,6)) - set(range(4,10))}")

        print(
            f"\n  set(range(4,10)) - set(range(1,6))   NOT IN  {set(range(4,10))} - {set(range(1,6))}  => {set(range(4,10)) - set(range(1,6))}")

        #SET not allow duplicates, 
        # IT CAN DO: LEN(), IN, MIN(), MAX(), UNION (|) , INTERSECT (&), NOT IN (-)
        
l_set = list_set()
l_set.set_op()
