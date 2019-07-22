
# tring module

import string

string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.octdigits
string.hexdigits
string.punctuation
a = "a"
print(f"\n a is letter: {a in string.ascii_letters}")

b = "123"
print(f"\n b is letter: {b in string.digits}")

# Exercise - is vowel, print lower case and upper case characters
isVowel = "a"
vowels = "aeiouAEIOU"
print(f"\n isVowel: { isVowel in vowels}")

'''
for char in string.ascii_uppercase:
    print(char)

for char in string.ascii_lowercase:
    print(char)


for char in string.digits:
    print(char)
'''


isconsonate = "b"
print(f"\n isConsonante: { isVowel not in vowels}")

print(f"{isconsonate.isalpha() and isconsonate.lower() not in vowels}")


#Excersices and Puzzles
string_example = "This is a split string"
string_example.split()

# Concact
print('1' * 20)
str = "test"
str2 = "test1"

print(str == str2)
str2 = "test"
print(str == str2)


#string Conclucion
