# Traversal of dictionary means visiting all key-value pairs of dictionary one-by-one.
# Reasons of Traversal
#   -Updating pairs
#   -Printing out values of keys

myDict = {"Name": "Priyanka", "Age": "26","Address":"Jaipur"}

def traversalDict(dict):
    for key in dict:
        print(key,dict[key])
    
traversalDict(myDict)