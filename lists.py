'''Lists
(1) Working with Lists
(2) List methods
(3) Lambda function
(4) enumerate, map and filter
'''

print("====== Working with Lists ========")
# Java | PhP | NodeJs > array => Python list

# literal
person = {"name": "Justin", "age": 23}  # Dictionary
people = ("Andrew", "Jhon", "Goppor")   # tuple
clubs = ["Barsa", "Real", "MU", "PSG"]  # list
for team in clubs:
    print(f"the team: {team}")

# constructor
letters = list("Hello World!")
print(f"the letters: {letters} and the size{len(letters)}")

print("-"*18)

fruits = ["apple", "peach", "cherry", "melon"]

a = fruits[0]
b = fruits[0:2]  # [0, 2)
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("====== List methods ========")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append letters: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert letters: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result2: {result2} and letters: {letters}")

print("-"*18)

animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")

print("-"*18)

numbers = [2, 20, 12, 8, 57]

numbers.sort()
print("sort default:", numbers)

numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable > sorted function & index() method

numbs = [2, 20, 12, 100]

new_numbs = sorted(numbs)

print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")

print("====== Lambda function ========")
# lambda is small anonymous function
def calculate(x, y): return x * y


result = calculate(3, 8)
print("result:", result)

people = [
    ("Robert", 27),
    ("Akmal", 33),
    ("Aziz", 12),
    ("Jhon", 22),
]
people.sort()
print("people(1)", people)

# Sort by age via Lambda

people.sort(key=lambda person: person[1])
print("people(2)", people)


print("====== enumerate, map and filter ========")
# enumerate is for index and value
animals = ["dog", "cat", "fish"]  # list

for element in enumerate(animals):
    print("element:", element)

for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")

print("------")

# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2025)  # dict
result = car_obj.items()

for (key, value) in result:
    print(f"the key: {key} and value: {value}")

print("------")

# map
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

new_cars = []

for car in cars:
    new_cars.append(car[0])

print("new_car:", new_cars)

result1 = map(lambda car: car[0], cars)

print(f"the result1: {result1} and type: {type(result1)}")
