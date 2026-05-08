# print("======= Numbers =========")

# In JAVA, variable is a name storage location
# In Python, vaiable is named reference!

# count = 100
# count_type = type(count)
# print("count:", count, count_type)
# print(f"the count: {count} and type {count_type}")

# result1 = count.bit_count()  # method

# result2 = count.numerator  # state
# print(result1, result2)


# print("======= string =========")

# # METHODS upper() lower() title() find() replace()

# course = "AI Python FullStack"

# result = type(course)
# print(f"the type of course(1): {result}")

# result = course.title()
# print(f"the result(2): {result}")

# result = course.upper()
# print(f"the result(3): {result}")

# result = course.replace("FullStack", "MasterClass")
# print(f"the result(4): {result}")

print("======= boolean =========")
# functions > type() input() bool() int() str()
y = input("Give your value for y: ")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

# TRUTHY vs FALSY value
# TRUTHY > True 100 -100 "MIT"
# FALSY > False 0 "" none

test_falsy = "" or False or 0 or None or 100
print("The Falsy:", bool(test_falsy))

test_truthy = "MIT"
print("The Falsy:", bool(test_truthy))
