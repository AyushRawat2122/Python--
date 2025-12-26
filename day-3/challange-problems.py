# problem 1 find out if a number is appeared more than once
# nums = [1, 2, 3, 2, 4, 2]

# def moreThanOnce(nums):
#     mp = dict()
#     for num in nums:
#         mp[num] = mp.get(num , 0) + 1
#         if mp[num] > 1:
#             return True
#     return False

# print(moreThanOnce(nums))

# ----------------------------------------------------------------------------------------------------------------------

# problem 2 generate a tuple from a list with even length string

# words = ["hi", "hello", "world", "python", "ok"]

# def tupleWithEvenStrings(words):
#     evenStrings = [word for word in words if len(word)%2 == 0]
#     return tuple(evenStrings)

# evenTuple = tupleWithEvenStrings(words)
# print(evenTuple)

# ----------------------------------------------------------------------------------------------------------------------

# problem 3

# You are given a list of integers.

# Tasks:

# Detect whether duplicates exist

# Create a set of unique elements

# Create a set of elements that appeared more than once

# 🔹 Input Example
# nums = [1, 2, 3, 2, 4, 1, 5]

# 🔹 Expected Output
# Duplicates exist: True
# Unique elements: {1, 2, 3, 4, 5}
# Duplicate elements: {1, 2}

nums = [1, 2, 3, 2, 4, 1, 5]

def moreThanOnce(nums):
    mp = dict()
    for num in nums:
        mp[num] = mp.get(num , 0) + 1
        if mp[num] > 1:
            return True
    return False

print(f"Duplicates exist: {moreThanOnce(nums)}")
uniqueElements = set(nums)
duplicateElements = set([num for num in nums if nums.count(num) > 1])
print(f"Unique elements: {uniqueElements}")
print(f"Duplicate elements: {duplicateElements}")

