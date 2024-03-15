# Del Keyword
# Time complexity of deleting a key-value pair using del keyword: O(1)
# Space complexity: O(1) - Deletion using del keyword does not require additional memory allocation.

print("1. Delete key-value pair using del keyword.")
dict1 = {1: 'apple', 2: 'banana', 3: 'cherry'}
print("Before deleting using Del Keyword: ", dict1)
del dict1[1]
print("After deleting using Del Keyword: ", dict1)
print()

# pop() method
# Time complexity of deleting a key-value pair using pop() method: O(1)
# Space complexity: O(1) - Deletion using pop() method does not require additional memory allocation.

print("2. Delete key-value pair using pop() method.")
dict2 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Before deleting using pop() method: ", dict2)
dict2.pop("age")
print("After deleting using pop() method: ", dict2)
print()

# popitem() method
# Time complexity of deleting the last key-value pair using popitem() method: O(1)
# Space complexity: O(1) - Deletion using popitem() method does not require additional memory allocation.

print("3. Delete last key-value pair using popitem() method.")
dict3 = {'name': 'John', 'age': 25, 'is_student': True, 'grades': [85, 90, 92]}
print("Before deleting using popitem() method: ", dict3)
dict3.popitem()
print("After deleting using popitem() method: ", dict3)
print()

# clear() method
# Time complexity of deleting all key-value pairs using clear() method: O(n)
# Space complexity: O(1) - Deletion using clear() method does not require additional memory allocation.

print("4. Delete all key-value pairs using clear() method.")
dict4 = {'name': 'Sarah', 'age': 28, 'city': 'Chicago', 'age': 29}
print("Before deleting using clear() method: ", dict4)
dict4.clear()
print("After deleting using clear() method: ", dict4)
print()
