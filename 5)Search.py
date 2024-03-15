# Find an element in the dictionary.
# There are many algorithms for seaching a given value in the dictionary.
# Use Linear search 
#   -Linear search is based on traversing a dictionary.
#   -Visit each and every element of dictionary and check if this is the value we are searching for.

myDict = {"Name": "Priyanka", "Age": 26}

def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "The value does not exist"

print(searchDict(myDict,26))
