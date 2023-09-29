# Lists

a = [1, 2, 3]
b = [4, 5, 6]

cars = [
    {
        "brand": "BMW", 
        "trim": "328i", 
        "color": "gray", 
        "price": 38900
    },
    {
        "brand": "Mercedes", 
        "trim": "350E", 
        "color": "white", 
        "price": 89000
    },
    {
        "brand": "Porsche", 
        "trim": "911", 
        "color": "orange", 
        "price": 95000
    },
    {
        "brand": "Kia", 
        "trim": "Sorento", 
        "color": "blue", 
        "price": 30900
    },
    {
        "brand": "Toyota",
        "trim": "Sienna", 
        "color": "gray", 
        "price": 51200
    },
]

composers = ["Beethoven", "Ravel", "Brahms", "Debussy", "Mahler", "Bruckner", "Mozart", "Bach", "Stravinsky"]


pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}
list1 = [1, 2, 3, 4]

# Get authenticator/decorator code from section materials

# def func1():
#     print("This is a function")

# # I can assign a function to a variable!
# another_func = func1
# another_func()

# def outer1(exp):
#     def inner(num):
#         return num ** exp
#     return inner
# add_exps = outer1(5)

# the above equals this
# def outer1(exp):
#     def inner(num):
#         return num ** 5
#     return inner

# result = add_exps(6)
# print(result)

# def outer(func):
#     print("Beginning the outer function")
#     def wrapper():
#         print("Beginning the wrapper function")
#         func()
#         print("Returning the wrapper function")
#     return wrapper

# def basic_func():
#     print("I'm just a basic function")

# result = outer(basic_func)
# result()

# Lambdas (anonymous functions)
# list1 = ["Neytiri", "Ronal", "Quaritch", "Tonowari", "Spider"]

# def add_ten(num):
#     return num + 10
# print(add_ten(10))

# x = lambda a : a + 10
# print(x(10))

# z = (lambda x : x + 5)(2)
# print(z)

# def five_ltr(list):
#     n = []
#     for i in list:
#         if len(i) == 5:
#             n.append(i)
#     return n

# print(five_ltr(list1))

# five_ltr_name = list(filter(lambda a : len(a) == 5, list1))
# print(five_ltr_name)

# Dictionaries list comprehension

# Return object
# cheap_cars = [car for car in cars if car["price"] < 40000]
# print(cheap_cars)

# Return value in key-value pair
# cheap_car_brands = [car["brand"].upper() for car in cars if car["price"] < 40000]
# print(cheap_car_brands)

# def find_orange(obj_list):
#     for obj in obj_list:
#         if obj["color"] == "orange":
#             print(obj)

# find_orange(cars)

# list_comprehension = [expression for item in iterable (if condition == True)]
# new_composers0 = [composer for composer in composers if "v" in composer]
# print(new_composers0)

# Same as above, just more lines of code and less elegant
# def v_composers(l):
#     new_composers = []
#     for composer in l:
#         if "v" in composer:
#             new_composers.append(composer)
#     print(new_composers)

# v_composers(composers)

# divmod -> tuple (quotient, remainder)
# result = divmod(101, 50)
# print(result)

# quotient, remainder = divmod(101, 50)
# print(f"Quotient: {quotient}")
# print(f"Remainder: {remainder}")

# Min-Max tuple
# def find_biggest_smallest(result):
#     return min(result), max(result)

# r = find_biggest_smallest(result)
# print(r)

# Tuples
# t = 'a', 'b', 'c', 'd', 'e'
# print(t)

# t1 = ('a', 'b', 'c', 'd', 'e')
# print(t1)

# Iteration through list of dictionaries
# def show_objects(objArr):
#     for obj in objArr:
#         for key in obj:
#             print(obj[key])
#         print()

# show_objects(cars)

# Iteration through list
# def list_composers(l):
#     for composer in l:
#         print(composer)

# list_composers(composers)

# Split
# my_str = "I love working in python!"
# my_str1 = "L-O-L"

# str_list = my_str.split()
# print(str_list)

# str_list1 = my_str1.split("-")
# print(str_list1)

# Slice
# s = composers[1:3]
# print(s)

# s1 = composers[:5]
# print(s1)

# s2 = composers[6:]
# print(s2)

# Length
# l = len(composers)
# print(l)

# Concatenation
# c = a + b
# print(c)

# Make list from tuple
# my_faves = list(("Steinway", "Bösendorfer", "Bechstein"))
# print(my_faves)
