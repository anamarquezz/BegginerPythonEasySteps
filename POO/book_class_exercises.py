# CLASSS CONTAIN ANOTHER CLASSS class Book with class of Reviews
class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        print("\n")
        return repr((self.id, self.name, self.author, self.reviews))

    def add_review(self, review):
        self.reviews.append(review)


class Review:
    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.id, self.description, self.rating))


book = Book(123, 'Object oriented Programming with Python', 'Ana Marquez')
print(book)
'''
review1 = Review(1, 'Great Book', 5)
print(review1)


book.add_review(review1) # add first review
print(f"book: {book}")

review2 = Review(2, 'bad Book', 1)  # add first review
book.add_review(review2)
print(f"book: {book}")
'''
book.add_review(Review(1, 'Great Book', 5))
book.add_review(Review(2, 'bad Book', 1))
print(f"book: {book}")
