## List Methods

| Method                | Description                    |
| --------------------- | ------------------------------ |
| `append()`            | Add one element                |
| `extend()`            | Add multiple elements          |
| `insert()`            | Insert at specific index       |
| `remove()`            | Remove by value                |
| `pop([i])`            | Remove by index (default last) |
| `clear()`             | Remove all                     |
| `sort(reverse=False)` | Sort list                      |
| `reverse()`           | Reverse elements               |
| `index(x)`            | Find index of x                |
| `count(x)`            | Count occurrences              |
| `copy()`              | Clone list                     |
| `len()`               | Length                         |
| `sum(), min(), max()` | Aggregation helpers            |
| `any(), all()`        | Boolean checks                 |

## Set Methods

| Method / Operation            | Description                                  |
| ---------------------------- | -------------------------------------------- |
| `add(elem)`                  | Add a single element                         |
| `update(iterable)`           | Add multiple elements from iterable          |
| `remove(elem)`               | Remove elem; raises KeyError if missing      |
| `discard(elem)`              | Remove elem if present (no error if absent)  |
| `pop()`                      | Remove and return an arbitrary element       |
| `clear()`                    | Remove all elements                          |
| `copy()`                     | Shallow copy of the set                      |
| `union(other)` / `|`         | Return union                                 |
| `intersection(other)` / `&`  | Return intersection                           |
| `difference(other)` / `-`    | Return difference                             |
| `symmetric_difference(other)` / `^` | Elements in one but not both         |
| `issubset(other)` / `<=`     | Check subset                                  |
| `issuperset(other)` / `>=`   | Check superset                                |
| `isdisjoint(other)`          | True if no common elements                    |
| `len()`                      | Number of elements                             |

## Tuple Methods

| Method / Operation      | Description                                    |
| ---------------------- | ----------------------------------------------- |
| `count(x)`             | Count occurrences of x                          |
| `index(x[, start[, end]])` | Return first index of x                      |
| `len()`                | Number of elements                               |
| `+` (concatenation)    | Join two tuples                                  |
| `*` (repetition)       | Repeat tuple                                     |
| Slicing               | Get subsequences (e.g., `t[1:3]`)                |
| Immutable             | Tuples are immutable; no item assignment        |