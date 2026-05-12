''' Objests
(1) What is object
(2) Iterible objects & RANGE
(3) DICTIONARY
(4) Error handling stystem
'''

import array  # package/module
import math
print("===== What is object =====")
# An object has state and method properties
# Everything is an object in Python!

print(type('Hello world!'))
print(type(100))
print(type(True))
print(type(array))

# Paradigm > Functional programming & OOP
# OOP 4 Concepts > Abstraction | Ecncapsulation | Inheritance | Polimorphism

result1 = math.ceil(92.8)  # CALL
print("result1:", result1)

result2 = math.ceil(99.9)
print("result2:", result2)


print("===== Error handling stystem =====")

car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passed here")
    result = car_dict["origin"]
    print("result:", result)

except Exception as err:
    print("General error:", err)


else:
    print("Exucuted successfully without errors")
finally:
    print("Final closing logic")
