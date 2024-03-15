# A dictionary is a mutable collection of key-value pairs where each unique key maps to a value.
# Dictionaries are implemented using hash tables, providing fast access to values based on their keys.

# Ways of creating an empty dictionary
# 1) Using the dict constructor
#    - Creates an empty dictionary.
#    - Time complexity: O(1)
#    - Space complexity: O(1)
my_dict = dict()
print(my_dict)

# 2) Using curly braces
#    - Creates an empty dictionary.
#    - Allocates memory only for the initial hash table structure.
#    - Time complexity: O(1)
#    - Space complexity: O(1)
my_dict2 = {}
print(my_dict2)

# Create a dictionary with elements
# Build a real dictionary that maps from English to Spanish words.
# Using the dict constructor
eng_sp = dict(One="Uno", Two="Dos", Three="Tres")
print(eng_sp)

# Using curly braces
eng_sp2 = {"One": "Uno", "Two": "Dos", "Three": "Tres"}
print(eng_sp2)

# Using a list of tuples
eng_sp3 = [("One", "Uno"), ("Two", "Dos"), ("Three", "Tres")]
print(eng_sp3)

# Time complexity for all these methods: O(N)
# Space complexity for all these methods: O(N)
