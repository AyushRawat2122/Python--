from collections import deque , Counter
# challenge 1 deque operations 
dq = deque()
# enqueue
dq.append(10)
dq.append(20)
dq.append(30)
dq.popleft()
dq.append(40)

print(dq[0])
print(dq)

# Challenge 2 — Reverse First K Elements
# You are given:
dq = deque([1, 2, 3, 4, 5])
k = 3
def swap(dq , i , j):
    dq[i] += dq[j]
    dq[j] = dq[i] - dq[j]
    dq[i] = dq[i] - dq[j]
    
def reverse_first_k_elements(dq, k):
    try:
        if len(dq) < k:
            raise Exception("k is supposed to be smaller than total length of dq")
        else:
            for i in range(k//2):
                swap(dq , i , k-1-i)
    except Exception as e:
        print(e)

reverse_first_k_elements(dq, k)
print(dq)

# Challenge 3 - charachter that appeared exactly once

s = "aabbccddefg"
def appearedOnce(cntr , s):
    for ch in s:
        if cntr[ch] == 1:
            return ch
    return None

cntr = Counter(s)
print(appearedOnce(cntr,s))