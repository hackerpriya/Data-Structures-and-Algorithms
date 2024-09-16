#Slicing is need in deletion of multiple elements from the list.
#Slice operator [:] is used to for slicing.
#By using slice operator we can update we can update multiple elements in the list.

myList = ['a','b','c','d','e','f','g','h']
print("List without slicing:",myList)
# print()
print("Both Start and End Index:",myList[0:2]) #0 is included and 2 is excluded from range of elements selected for slicing.
# print()
print("Start Index ommitted:",myList[:2])  #0 will first index by default
# print()
print("End Index ommitted:",myList[1:])  #Last index will be end index by default
# print()
print("Both Start and End Index ommitted:",myList[:])   #0 will be first index & last index will be end index by default
print()


#Update List using Slice Operator
print("Before Updating List:",myList)
myList[0:3] = ['x','y','z']
print("After Updating 3 elements of List:",myList)
print()


#Deletion of Element in List
#Delete using pop() method with index
print("Before Deletion:",myList)
myList.pop(1)   #1 is index of element to be deleted
print("After Deletion:",myList)
print("Time complexity: O(N) as each index will have to shift one step further.")
print("Space Complexity: O(1)")
print()

#Delete using pop() method without index
print("Before Deletion:",myList)
myList.pop()  #Delets last element
print("After Deletion:",myList)
print("Time complexity: O(1)")
print("Space Complexity: O(1)")
print()


#Delete using del keyword with index
print("Before Deletion:",myList)
del myList[3]
print("After Deletion:",myList)
print("Time complexity: O(N) as rest elements have to move one step or more steps to the left.")
print("Space Complexity: O(1)")
print()

#Delete multiple elements using del keyword with slicing operator
print("Before Deletion:",myList)
del myList[0:3]
print("After Deletion:",myList)
print("Time complexity: O(N) as rest elements have to move one step or more steps to the left.")
print("Space Complexity: O(1)")
print()

#Delete using remove() method by specifying value
print("Before Deletion:",myList)
myList.remove('f')
print("After Deletion:",myList)
print("Time complexity: O(N) as rest elements have to move one step or more steps to the left.")
print("Space Complexity: O(1)")
print()
