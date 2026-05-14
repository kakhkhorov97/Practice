''' Tuples
(1) What is Tuple: tuple vs list 
(2) Unpacking arguments
(3) zip
'''


print("====== What is Tuple: tuple vs list  ========")

# Java | PhP | NodeJs > array => Python list

# Literal
numbs = [3, 5, 7, 1]

# Constructor

letters = list("Hello World!")

fruits = ["apple", "peach", "lemon", "cherry"]
print("before fruits:", fruits)

fruits[3] = "melon"

print("-"*18)

print("after fruits:", fruits)

print("-"*18)
# we can not mutate TUPLE

animals = ("dog", "cat", "horse", "zebra")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "Bird"

print("-"*18)

# Try to avoid these
people = "Jhon", "Jack"
animals = "dog", "cat"

print("====== Unpacking arguments ========")

clubs = ["Barca", "Real", "MU", "PSG"]
(x, y, *z) = clubs
print(f"the x: {x} and the y: {y}")

print("-"*18)

print("z:", z)  # list


# *args > tuple

def calculate(*args):
    total = 1
    for x in args:
        total *= x
        print(f"the total value: {total}")
        return total


# CALL

calculate(3, 22, 8, 2)
calculate(8, 83, 12, 4)
calculate(7, 10,)

print("-"*18)

# *kwargs > dictionary


def introduce(**kwargs):
    # print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I'm {kwargs["name"]} and I'm {kwargs["age"]}years old")


# CALL

introduce(name="Shawn", age=28)
introduce(name="Tom", age=42, single=True)


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


# CALL
greeting("hi", True, 100, name="Stive", age=22)


print("====== zip ========")

tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c', 'd')

zipped = zip(tuple1, tuple2)
print("zipped:", zipped)
result = list(zipped)
print(f"the result: {result}")
