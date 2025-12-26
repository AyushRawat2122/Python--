## Dictionary Methods

| Method                          | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| `get(key[, default])`           | Get value by key (returns default if not found) |
| `keys()`                        | Return all keys                                  |
| `values()`                      | Return all values                                |
| `items()`                       | Return key-value pairs as tuples                 |
| `update(other)`                 | Merge another dict or iterable of pairs          |
| `pop(key[, default])`           | Remove and return value for key                  |
| `popitem()`                     | Remove and return last (key, value) pair         |
| `clear()`                       | Remove all items                                 |
| `copy()`                        | Shallow copy of dictionary                       |
| `setdefault(key[, default])`    | Get key value; set to default if not present     |
| `fromkeys(seq[, value])`        | Create dict from sequence with optional value    |
| `len()`                         | Number of key-value pairs                        |
| `in` / `not in`                 | Check if key exists                              |
| `del dict[key]`                 | Delete key-value pair                            |
| Dict comprehension              | `{k: v for k, v in ...}`                         |

## Usage Examples

```python
# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "NYC"}

# get() - safe access
print(person.get("name"))           # Alice
print(person.get("email", "N/A"))   # N/A (default)

# keys(), values(), items()
print(person.keys())                # dict_keys(['name', 'age', 'city'])
print(person.values())              # dict_values(['Alice', 25, 'NYC'])
print(person.items())               # dict_items([('name', 'Alice'), ...])

# update() - merge dictionaries
person.update({"age": 26, "email": "alice@example.com"})
print(person)                       # {'name': 'Alice', 'age': 26, 'city': 'NYC', 'email': '...'}

# pop() - remove and return
age = person.pop("age")
print(age)                          # 26

# popitem() - remove last inserted
last_item = person.popitem()
print(last_item)                    # ('email', 'alice@example.com')

# setdefault() - get or set default
person.setdefault("country", "USA")
print(person)                       # {'name': 'Alice', 'city': 'NYC', 'country': 'USA'}

# fromkeys() - create dict from keys
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)                     # {'a': 0, 'b': 0, 'c': 0}

# Checking membership
print("name" in person)             # True
print("age" in person)              # False

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)                      # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Iterating through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# copy() - shallow copy
person_copy = person.copy()

# clear() - remove all
person_copy.clear()
print(person_copy)                  # {}
print(person)                       # Original unchanged
```
