from collections import deque , OrderedDict , Counter , defaultdict , namedtuple 
# Other collections deque {double ended queue} / Counter / defaultdict(list) / namedtuple / ordereddict 

# deque stands for double ended queue which allows you to add or remove elements from both ends efficiently.
# -------------------------------------------------------------------------------------
# Example of deque
dq = deque(['a', 'b', 'c'])
dq.append('d')          # Add to the right end
dq.appendleft('z')      # Add to the left end
print(dq)               # Output: deque(['z', 'a', 'b', 'c', 'd'])
dq.pop()                # Remove from the right end 
dq.popleft()            # Remove from the left end
print(dq)               # Output: deque(['a', 'b', 'c'])
len_dq = len(dq)        # Get the length of the deque
print(len_dq)           # Output: 3
# --------------------------------------------------------------------------------------
# Example of Counter
data = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 2})
print(counter['apple'])  # Output: 3
print(counter.most_common(1))  # Output: [('apple', 3)] most common element in counter 
print(counter.most_common(2))  # Output: [('apple', 3), ('banana', 2)] most common 2 elements in counter
# --------------------------------------------------------------------------------------
# Example of defaultdict
dd = defaultdict(int)  # Default value of int is 0
dd['a'] += 1
dd['b'] += 2    
print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
# --------------------------------------------------------------------------------------
# Example of namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p)  # Output: Point(x=11, y=22)
print(p.x, p.y)  # Output: 11 22
# --------------------------------------------------------------------------------------
# Example of OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)  # Output: OrderedDict([('a', 1), ('b', 2)])
od.move_to_end('a')  # Move 'a' to the end
print(od)  # Output: OrderedDict([('b', 2), ('a', 1)])
# --------------------------------------------------------------------------------------
# These collections provide specialized data structures that can be very useful in various scenarios.