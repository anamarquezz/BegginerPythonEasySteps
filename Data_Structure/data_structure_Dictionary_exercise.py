class dictionary_data_exercise:
    def __init__(self):
        self.str = "This is an awesome occasion, This has never happened before."

    def set_dict(self):
        print(f"\n\n {self.str} \n")

        # key:value

        char_occurances = {}  # []

        for char in self.str:  # how many times apper the character
            char_occurances[char] = char_occurances.get(char, 0) + 1
        print(char_occurances)

        word_occurances = {}
        for word in self.str.split():  # how many times apper the word
            word_occurances[word] = word_occurances.get(word, 0) + 1
        print(word_occurances)

        squares_first_ten_numbers = [i*i for i in range(1, 11)]
        print(
            f"\n\nsquares_first_ten_numbers => {type(squares_first_ten_numbers)}")
        print(
            f"squares_first_ten_numbers => {squares_first_ten_numbers}")

        squares_first_ten_numbers_set = set(squares_first_ten_numbers)
        squares_first_ten_numbers_set = {i*i for i in range(1, 11)}
        print(
            f"\n\nsquares_first_ten_numbers_set => {type(squares_first_ten_numbers_set)}")
        print(
            f"squares_first_ten_numbers_set => {squares_first_ten_numbers_set}")

        squares_first_ten_numbers_dict = {i: i*i for i in range(1, 11)}
        print(
            f"\n\nsquares_first_ten_numbers_dict => {type(squares_first_ten_numbers_dict)}")
        print(
            f"squares_first_ten_numbers_dict => {squares_first_ten_numbers_dict}")

        print(f"\n\n TYPES:  \n type([]) => {type([])}")
        print(f"type(set()) => {type(set())}")
        print(f"type(set({{1}})) => {type({1}) }")
        print(f"type({{}}) => {type({})}")
        print(f"type({{'A':5}}) => {type({'A':5})}")


l_set = dictionary_data_exercise()
l_set.set_dict()
