''' Operators & Conditions
(1) Operators
(2) Conditons 
(3) Logical operators
'''
print("===== Operators ========")
# = - > >= < <= * /  //% += **

a = 19
b = 5

print(a/b)
result = a // b
left = a % b
print(f"the result: {result} and the left: {left}")

# a = a * 100
a += 100
print("a:", a)
print("b**2", b**2)
print("b**3", b**3)

print("="*5)

c = dict(name: "Shawn", age: 28)
d = dict(name: "Shawn", age: 28)
e = c

print("c==d", c == d)  # only value
print(id(c), id(e), id(d))

print("c is d", c is d)
print("c is e", c is e)


print("===== Conditons ========")
x = 15
if x > 50:
    print("case A")
elif x > 10:
    print("case B")
else:
    print("case C")

print("===== Logical operators ========")

age = 21
# person = None
# if age > 16:
#     person = "adult"
# else:
#     person = "minor"


# Ternary
person = "adult" if age > 18 else "minor"
print("person:", person)

print("-----")

# Boolean variables
is_student = True
is_admin = False
is_guest = True
is_parent = False

# Conditions
if not is_student:
    print("Wellcome here, do you want to be student!")
elif is_admin:
    print("Please go to this office!")
elif is_guest or is_parent:
    print("Waiting room is over there!")
else:
    print("Other cases")
