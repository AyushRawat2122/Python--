# ⚔️ Mini Practice #1 — List Basics

games = ["Valorant", "GTA V", "Minecraft", "Apex Legends", "Witcher 3"]

print("1️⃣ My Favorite Games:", games)
print("2️⃣ First Game:", games[0])
print("3️⃣ Last Game:", games[-1])

games[2] = "Cyberpunk 2077"
print("4️⃣ Updated List:", games)

games.append("Sekiro")
print("5️⃣ Added New Game:", games)

games.pop(1)
print("6️⃣ Removed 2nd Game:", games)

print("7️⃣ Total Games:", len(games))

# Properties of Lists
# - Ordered maintain order unlike set (like all elements just thrown inside a box its like a bookshelf all books kept in order - makes easy access)
# - Mutable can be modified like add or remove elements after creation
# - Heterogenous (Scientific term - it means mixture of different varitey) which means you can do like this ["Ayush Rawat", 23, false]
# - Duplicate elements allowed
# - Indexable and Sliceable : Indexable -> access with index games[0], Sliceable -> can slice like nums[1:4] give list of three elements ['Cyberpunk 2077', 'Apex Legends', 'Witcher 3']
# - Dynamic size: add or remove elements | Iteratable: can loop them | Nestable: list can contain other list (multi-dimensional).
# - Support Many Built-in Methods like append(), sort(), reverse()
# - Sorted by Reference (not value) means a = ['20','30'] 
#                                         b = a
#                                         b.pop() => if we print a ['20'] <- bye bye 30  || for deep copy b = a.copy() => now they are individual
    
# Ways to create list


# 1️⃣ Literal method (standard)
nums = [1, 2, 3, 4]
print("Literal list:", nums)

# 2️⃣ Using list() constructor with different iterables

# From string
chars = list("Ayush")
print("From string:", chars)

# From tuple
nums_from_tuple = list((10, 20, 30))
print("From tuple:", nums_from_tuple)

# From range
nums_from_range = list(range(5))
print("From range:", nums_from_range)

# From set
nums_from_set = list({7, 8, 9})
print("From set (unordered):", nums_from_set)

# 3️⃣ Empty lists
a = []         # Literal way
b = list()     # Constructor way
print("Empty list A:", a)
print("Empty list B:", b)

# 4️⃣ Special trick — list repetition
repeat = [0] * 5
print("Repeated elements:", repeat)

# 5️⃣ Nested list (2D)
matrix = [[1, 2, 3], [4, 5, 6]]
print("Nested list:", matrix)

# Output
# Literal list: [1, 2, 3, 4]
# From string: ['A', 'y', 'u', 's', 'h']
# From tuple: [10, 20, 30]
# From range: [0, 1, 2, 3, 4]
# From set (unordered): [8, 9, 7]
# Empty list A: []
# Empty list B: []
# Repeated elements: [0, 0, 0, 0, 0]
# Nested list: [[1, 2, 3], [4, 5, 6]]

# any | some {js} and all | every {js}
# any() -> returns True if at least one element is truthy
# all() -> returns True if all elements are truthy

attempts = [
    "admin",
    "root3",
    "user",
    12345,
    "john_doe",
    "ab1"
]

def validateEntries(entry):
    if isinstance(entry, str) and len(entry) <= 5:
        print(len(entry))
        return True
    else :
        return False

print(f"Falty Entries : { all(validateEntries(entry) for entry in attempts) }")

# Set and tuple with the constructor

ct = tuple([1,2,3,4])
cs = set(ct)
print(ct , cs)


# 🟦 TUPLE METHODS
t = (1, 2, 2, 3)

t.count(2)        # returns number of times 2 appears → 2

t.index(3)        # returns index of first occurrence of 3 → 3

# 🟩 SET METHODS
s = {1, 2, 3}
t = {3, 4, 5}

s.add(4)          # adds element to set

s.remove(2)       # removes element, error if not present

s.discard(10)     # removes element, NO error if not present

s.pop()           # removes and returns a random element

s.clear()         # removes all elements

s.copy()          # returns a shallow copy of set

s.union(t)        # returns new set with all elements from both sets

s.intersection(t) # returns common elements of both sets

s.difference(t)   # elements in s but not in t

s.symmetric_difference(t)
# elements present in either set but NOT both

s.update(t)       
# adds elements of t into s (modifies s)

s.intersection_update(t)
# keeps only common elements in s

s.difference_update(t)
# removes elements from s that are also in t

s.symmetric_difference_update(t)
# updates s with symmetric difference

s.issubset(t)     # checks if s ⊆ t → True / False

s.issuperset(t)   # checks if s ⊇ t → True / False

s.isdisjoint(t)   # True if no common elements