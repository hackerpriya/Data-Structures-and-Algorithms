# Time complexity of Inserting key-value pair = O(1)
# Space Complexity of Inserting key-value pair = amortized O(1)
#   - It changes to O(n) when underlying data structure needs to grow or shrink.
#   - As the latter only happens infrequently, people use the word "amortized".
#   - For example, if we add pairs to the dictionary and the capacity of the dictionary is reached, the space allocation is doubling.
#   - That's why space complexity becomes O(1).
#   - That's why it is called amortized O(1).

# Declare Dictionary
myDict = {"Name": "Priyanka", "Age": "26"}

# Update value of key in dictionary
print("1. Update value of key in dictionary")
print("⚫ Dictionary before updating value:", myDict)
myDict["Age"] = 27
print("⚫ Dictionary after updating value:", myDict)
print()

# Insert key-value pair in dictionary
print("2. Insert value of key in dictionary")
print("⚫ Dictionary before inserting key-value pair:", myDict)
myDict["Address"] = "Jaipur"
print("⚫ Dictionary after inserting key-value pair:", myDict)
print()
