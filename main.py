# 14.03.2021

# from random import shuffle
#
#
# class Card:
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value
#
#     def __repr__(self):
#         return "{} of {}".format(self.value, self.suit)
#
#
# class Deck:
#     def __init__(self):
#         suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#         values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#         self.cards = [Card(suit, value) for suit in suits for value in values]
#
#     def __repr__(self):
#         return "Cards remaining in deck: {}".format(len(self.cards))
#
#     def shuffle(self):
#         if len(self.cards) < 52:
#             raise ValueError("Only full decks can be shuffled")
#         shuffle(self.cards)
#         return self
#
#     def deal(self):
#         if len(self.cards) == 0:
#             raise ValueError("All cards have been dealt")
#         return self.cards.pop()


# 28.01.2021

# from datetime import datetime
#
# global_id = 1
#
#
# class Note:
#     id: int
#     memo: str
#     tags: list
#     creation_date: datetime
#
#     def __init__(self, memo: str, tags: list):
#         global global_id
#         self.memo = memo
#         self.tags = tags
#         self.creation_date = datetime.now()
#         self.id = global_id
#         global_id += 1
#
#     def match(self, own_filter: str):
#         for word in self.memo.split():
#             if word == own_filter:
#                 return True
#         for tag in self.tags:
#             if tag == own_filter:
#                 return True
#         return False
#
#
# class Notebook:
#     notes: list
#
#     def new_note(self, memo: str, tags: list):
#         note = Note(memo, tags)
#         self.notes.append(note)
#
#     def modify_memo(self, note_id: int, new_memo: str):
#         for note in self.notes:
#             if note.id == note_id:
#                 note.memo = new_memo
#
#     def modify_tags(self, note_id: int, new_tags: list):
#         for note in self.notes:
#             if note.id == note_id:
#                 note.tags = new_tags
#
#     def match(self, own_filter: str):
#         result = []
#         for note in self.notes:
#             if note.match(own_filter):
#                 result.append(note)
#         return result

# task 2

# import math
#
#
# class Point:
#     primary_value: tuple
#     coordinates: tuple
#
#     def __init__(self, *args):
#         self.coordinates = args
#         self.primary_value = args
#
#     @staticmethod
#     def __are_tuples_equal(lhs, rhs) -> bool:
#         return True if len(lhs) == len(rhs) else False
#
#     def move_to(self, *args):
#         self.coordinates = args
#
#     def show_coordinates(self):
#         print(self.coordinates)
#
#     def reset(self):
#         self.coordinates = self.primary_value
#
#     def distance(self, p2):
#         if not self.__are_tuples_equal(self.coordinates, p2.coordinates):
#             return
#
#         result = 0
#         for index in range(0, len(p2.coordinates)):
#             a = p2.coordinates[index]
#             b = self.coordinates[index]
#             result += pow(a + b, 2)
#         print(math.sqrt(result))
#
#
# p = Point(1, 4, 6, 8, 9)
# p.show_coordinates()
# p.move_to(1, 6, 8, 9, 3)
# p.show_coordinates()
# p.reset()
# p.show_coordinates()
#
# x = Point(1, 5, 8, 9, 3)
# p.distance(x)
