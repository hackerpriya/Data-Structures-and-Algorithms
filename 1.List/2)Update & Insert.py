#Lists are mutable data structures that's why you can change the order of elements in a list or reassign an item in a list.
#Braket operator appear on the left side of an assignment,it identifies the element of the list that will be assigned.
#Lists are ordered collections, meaning that order of element will be same order as we declare them till we change the order.

myList = [1,2,3,4,5,6,7]
print("Before Updating List:",myList)
print()

#Update element of list.
myList[2] = 27  #use bracket operator
myList[5] = 30
print("After Updating List:",myList)
print()


#Time and Space complexity
#Time complexity for accessing element of list = O(1)
#Space Complexity = O(1)        because no extra memory space needed.



#Insert element of List
print("Insert element at beginning or any specific position using insert()")
#Insert method inserts an element in any given location to the list.It moves each element's index one step further.
print("Before Insertion:",myList)
myList.insert(0,11)  #----->Time Complexity= O(N) ,0 is index and 11 is element
print("After Insertion:",myList)
print()

print("Insert element at the end by using append() method")
print("Before Insertion:",myList)
myList.append(55) #----->Time Complexity = O(1),Space Complexity = O(1)
print("After Insertion:",myList)
print()


#Extend method
#Extend method add another list to our list.
print("Extend list using extend() method")
newList = [12,13,14,15]
print("Before Extending:",myList)
myList.extend(newList)  #------>Time Complexity = O(N) , Space Complexity = O(N)
print("After Extending:",myList)
print()


