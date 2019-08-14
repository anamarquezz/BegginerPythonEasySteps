class dictionary_data:
    def __init__(self):
        self.occurances = dict(a=5, b=6, c=8, d=15)

    def set_dict(self):
        print(f"\n {self.occurances}")
        self.occurances['d'] = 15
        print(f"\n self.occurances['d']=15")
        print(f"\n occurances['d'] => {self.occurances['d'] }")
        self.occurances['d'] = 10
        print(f"\n self.occurances['d'] = 10")
        print(f"\n occurances['d'] => {self.occurances['d'] }")
        print(f"\n occurances['e'] => keyError: 'e' No existe ")

        print(f"\n\n occurances.get('d') => {self.occurances.get('d')} ")
        print(
            f"\n occurances.get('e') no existe pero no hay error => {self.occurances.get('d')} ")
        print(
            f"\n occurances.get('e') no existe y remplazar => {self.occurances.get('d',10)} ")
        print(f"\n occurances => {self.occurances}")

        print(f"\n\n occurances.keys() => {self.occurances.keys()}")
        print(f"\n occurances.values() => {self.occurances.values()}")
        print(f"\n occurances.items() => {self.occurances.items()}")

        print(f"\n\nLOOP")
        for (key, value) in self.occurances.items():
            print(f"{key}: {value}")

        print(f"\n\nDelete")

        print(f"\n self.occurances => { self.occurances}")
        del self.occurances['a']
        print(f"\n del self.occurances['a'] => { self.occurances}")


l_set = dictionary_data()
l_set.set_dict()
