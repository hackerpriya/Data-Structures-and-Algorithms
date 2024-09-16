#Two ways of Searching

#Declaring List
myList = [10,20,30,40,50,60,60,70,80,90]

#First Way : in operator
#in operator checks an element within a sequence by iterating through a sequence and comparing each element to the target value.
#If target value is found, the search is successful and it returns true else returns false.
#in operator has better time complexity when used with sets and dictionary which are implemented as hash tables.However using a set and dictionary requires additional spaces and looses information about the order and inxex of the element.
target = 50
target2 = 500
print("First Way : in operator")
if target in myList:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")
print("Time Complexity of in operator : O(N) in the worst case because python performs linear search")
print()


#Second Way : Linear Search
#Enumerate get the pairs of the index and value from this list.
#Enumerate function iterate over the list while also keeping the track of the index of the current item.
#Here we can easily get index of current element.
def linear_search(p_list,p_target):
    for i, value in enumerate(p_list): #---->Time Complexity : O(N)
        if value ==p_target: #---->Time Complexity : O(1)
            return i         #---->Time Complexity : O(1)
    return -1                #---->Time Complexity : O(1)

print("Second Way : Linear Search:",linear_search(myList,target))
print("Second Way : Linear Search:",linear_search(myList,target2))
print("Time Complexity of Linear Search : O(N) as it loops through all elements of the list with enumerate.")
print("Space Complexity of Linear Search : O(1) as it no extra memory space required.")
print()
