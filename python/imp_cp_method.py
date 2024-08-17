from collections import deque
from itertools import accumulate

# # Create a list of numbers
numbers = [4, 2, 5, 1, 3]

# Sorting the list
sorted_numbers = sorted(numbers)
print("Sorted:", sorted_numbers)

# Finding an element
found = 3 in sorted_numbers
print("3 is found in the list:", found)

# Using deque for a double-ended queue
dq = deque(numbers)
dq.appendleft(0)
dq.append(6)
print("Deque:", dq)

# Using accumulate
accumulated = list(accumulate(numbers))
print("Accumulated:", accumulated)

# Counting occurrences of an element
count_2 = numbers.count(2)
print("Count of 2:", count_2)

# Iterate over an iterable and get the index and value.
for index, value in enumerate(numbers):
    print(index, value)
number = [4, 2, 5, 1, 3]

from collections import Counter
count = Counter(numbers)

sorted_by_absolute = sorted(number, key=abs)

n = 10  # Define the length of the list

# Method 1: Using List Comprehension
zero_list_comprehension = [0 for _ in range(n)]
print("List using list comprehension:", zero_list_comprehension)

# Method 2: Using Multiplication
zero_list_multiplication = [0] * n
print("List using multiplication:", zero_list_multiplication)

''' getting squared sum of each element in list'''
numbers = [1, 2, 3, 4, 5]  # Example list

squared_sum = sum([x**2 for x in numbers])
print(f"The squared sum is: {squared_sum}")
