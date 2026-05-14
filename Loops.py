''' Loop operators 
(1) For 
(2) Break/Else
(3) While
'''
print("====== For Operators ========")

# Iterable objects > string | dict | tuple | list | range | map | filter

text = "MIT"
numbs = [8, 5, 3, 4]
car_obj = dict(brand="Cobalt", Year=2026)
range_obj = range(5)  # [0-5)

for letter in text:
    print(f"the letter:{letter}")

print("-"*18)

for number in numbs:
    print(f"the number:{number}")

print("-"*18)

for key in car_obj:
    print(f"the key:{key} => value: {car_obj.get(key)}")

print("-"*18)


print("====== Break/Else ========")

for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("Reached break")
        break
else:
    print("Exucuted successfully")

print("-"*18)

print("====== While Operator ========")

numb = 40
while numb > 0:
    numb -= 10
    print(f"the numb equals {numb}")

print("-"*18)

count = 0
while True:
    count += 1
    x = int(input("Find the number"))

    if x == 6:
        print(f"You found the number {count} attempts")
        break
    else:
        print("Wrong, try again!")
