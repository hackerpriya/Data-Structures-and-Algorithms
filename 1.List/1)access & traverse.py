#Syntax for accessing the elements of a list is the same as for accessing the elements of an array.
# Here we will use bracket operator.
# [index] : The expression inside bracket will be index.
# Think of a list as a relationship between indexed and elements.This relationship is called mapping.
# Each index maps to the one of the elements.List index work the same as array indexes.
#Any integer expression can be used as index.
#len() function returns number of items within a container.


#1. Access 
#1.1. Access elements through index number.
print("1.1. Access elements through index number.")
shoppingList = ['Milk','Cheese','Butter']
print(shoppingList[0])
print(shoppingList[1])
print()  #Line space

#1.2. Check if an element exists in the list or not by using in operator.
print("1.2. Check if an element exists in the list or not by using in operator.")
print('Milk' in shoppingList)
print('Bread' in shoppingList)
print() #Line Space

#1.3. Access elements from backward by using Negative Index.
print("1.3. Access elements from backward by using Negative Index.")
print(shoppingList[-1]) 
print() #Line Space




#2. Traverse 
#2.1. Traverse the elements of a list with loop.
print("2.1. Traverse the elements of a list with loop.")
for i in shoppingList: # i will visit each element of list
    print(i)
print()

#2.2. Traverse the elements through indexes of a list with range() function.(Useful to perform mathematical operations on list)
print("2.2. Traverse the indexes of elements of a list with range() function.")
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
print()

#2.3. Traverse through empty list.
print("2.3. Traverse through empty list.")
empty = []
for i in empty:
    print("I am empty")
print()