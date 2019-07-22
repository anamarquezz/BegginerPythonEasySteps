numbers = [1, 4, 6, 3, 4]
for number in numbers:
    print(number)

print("enumerate number")
for index, number in enumerate(numbers):
    print(f"{index} - {number}")

print("enumerate string")

values = list('aeiou')

for index, vowel in enumerate(values):
    print(f"{index} - {vowel}")
