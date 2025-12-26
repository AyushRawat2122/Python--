# Challange Questions + Py new Collection - Dictionary
# dictionaries are used to store data values in key:value pairs.

mp = {
    "name": "John",
    "age": 30,
    "city": "New York"
} # literal
mp2 = dict(name="John", age=30, city="New York") # constructor

print(mp)
print(mp2)

# Looping and iterating through a dictionary

for key in mp:
    print(key, ":", mp[key])

for value in mp.values():
    print(value)
    
for key,value in mp.items():
    print(key, "->", value)
    
for value , key in enumerate(mp):
    print(value, "->", key , ":", mp[key])
    
# Adding new items to a dictionary
mp["email"] = "john@example.com"
mp.update({"phone": "123-456-7890"} , {"age": 31}) # also updates age
print(mp)

# methods
print(mp.get("name")) # John
print(mp.keys()) # dict_keys(['name', 'age', 'city', 'email', 'phone'])
print(mp.values()) # dict_values(['John', 31, 'New York', 'john@example.com', '123-456-7890'])
print(mp.items()) # dict_items([('name', 'John'), ('age', 31), ('city', 'New York'), ('email', 'john@example.com'), ('phone', '123-456-7890')])
print(len(mp)) # 5
mp.pop("age") # removes age
print(mp)
mp.popitem() # removes last inserted item
print(mp)
del mp["city"] # removes city
print(mp)
mp.clear() # clears the dictionary
print(mp) # {}

# 🔥 DICTIONARY COMPREHENSION (POWER MOVE)
squares = {x: x*x for x in range(5)}
even_map = {x: x for x in range(10) if x % 2 == 0}

print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(even_map) # {0: 0, 2: 2, 4: 4, 6: 6, 8: 8}