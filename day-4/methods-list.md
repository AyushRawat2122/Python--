## deque Methods
| Method/Attribute                | Description                                    |
| ------------------------------ | ---------------------------------------------- |
| `append(x)`                    | Add to right end                               |
| `appendleft(x)`                | Add to left end                                |
| `extend(iterable)`             | Add multiple to right                          |
| `extendleft(iterable)`         | Add multiple to left (reversed order)          |
| `pop()`                        | Remove and return rightmost                    |
| `popleft()`                    | Remove and return leftmost                     |
| `remove(value)`                | Remove first occurrence                        |
| `clear()`                      | Remove all elements                            |
| `rotate(n=1)`                  | Rotate right by n (left if negative)           |
| `reverse()`                    | In-place reverse                               |
| `count(x)`                     | Count occurrences                              |
| `index(x[, start[, stop]])`    | Find index of x                                |
| `insert(i, x)`                 | Insert at position i                           |
| `copy()`                       | Shallow copy                                   |
| `maxlen`                       | Read-only max length                           |
| `len(dq)`                      | Number of elements                             |

### deque Usage
```python
from collections import deque

dq = deque(['a', 'b', 'c'], maxlen=5)
dq.append('d'); dq.appendleft('z')
dq.extend(['e', 'f'])           # respects maxlen
dq.rotate(1)                    # right rotate
print(dq)                       # deque(['f', 'z', 'a', 'b', 'c'])
dq.remove('z'); dq.reverse()
```

## Counter Methods
| Method/Operation               | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| `Counter(iterable|mapping)`   | Create counter                                 |
| `most_common([n])`            | Top n pairs                                    |
| `elements()`                  | Iterator repeating elements by count           |
| `update(iter|map)`            | Add counts                                     |
| `subtract(iter|map)`          | Subtract counts                                |
| `total()`                     | Sum of counts (Py ≥ 3.10)                      |
| `clear(), copy()`             | Manage state                                   |
| `c1 + c2, c1 - c2`            | Add/subtract counters                          |
| `c1 & c2, c1 | c2`            | Min/Max per key                                |
| Dict methods                  | `keys()`, `items()`, `get()`, etc.             |

### Counter Usage
```python
from collections import Counter

c = Counter(['apple', 'banana', 'apple'])
c.update({'banana': 2, 'orange': 1})
print(c.most_common(2))         # [('apple', 2), ('banana', 3)]
print(list(c.elements()))       # ['apple', 'apple', 'banana', 'banana', 'banana', 'orange']
d = Counter('banana')
print(c & d, c | d)             # min/max per key
```

## defaultdict Methods
| Method/Attribute               | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| `defaultdict(factory)`        | Create with default factory                    |
| `default_factory`             | The factory used to create missing values      |
| `__missing__(key)`            | Called to create default (internal)            |
| Dict methods                  | All dict operations (`get`, `update`, etc.)    |

### defaultdict Usage
```python
from collections import defaultdict

dd = defaultdict(int)
dd['a'] += 1                     # creates 0 then +1
dd = defaultdict(list)
dd['grp'].append('item')
print(dd['missing'])             # [] auto-created
```

## namedtuple Methods
| Method/Attribute               | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| `namedtuple(name, fields)`    | Create tuple subclass                          |
| `_make(iterable)`             | Build instance from iterable                   |
| `_replace(**kwargs)`          | Return new instance with fields replaced       |
| `_asdict()`                   | Ordered dict of field values                   |
| `_fields`                     | Tuple of field names                           |
| `_field_defaults`             | Defaults mapping (if provided)                 |
| `_source`                     | Generated class source (if available)          |
| Tuple ops                     | Indexing, slicing, `count`, `index`            |

### namedtuple Usage
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p.x, p[1])                 # 11, 22
p2 = p._replace(y=99)
print(p2._asdict())              # {'x': 11, 'y': 99}
```

## OrderedDict Methods
| Method/Operation               | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| `OrderedDict()`               | Insertion-ordered dict                         |
| `move_to_end(key, last=True)` | Move key to end or beginning                   |
| `popitem(last=True)`          | Pop last (or first) item                       |
| Iteration order               | Preserves insertion order                      |
| Dict methods                  | All standard dict methods                      |
| `reversed(od)`                | Iterate keys in reverse                        |

### OrderedDict Usage
```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1; od['b'] = 2; od['c'] = 3
od.move_to_end('a')              # end
print(list(od.items()))          # [('b', 2), ('c', 3), ('a', 1)]
first = od.popitem(last=False)   # ('b', 2)
```
