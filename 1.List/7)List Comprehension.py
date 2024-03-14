#List comprehension is very useful for python developers because it cuts down on the amount of the typing and makes code shorter.
#List comprehension is easier to read.
#List comprehension is a where you create a new list from the previous list.


#We are creating a list from other lists using for loops.
prev_list = [1,2,3]
new_list = []
print("Before creating list using loop : ",new_list)
for i in prev_list:
    multiply_2 = i*2
    new_list.append(multiply_2)
print("After creating list using loop  : ",new_list)
print()

#List Comprehension on List.
#Using list comprehension,we can take 4 lines of above code and turn into one line.
#Expression of List Comprehension : new_list = [new_item for item in list]
#list = prev_list , item = i , new_item = expression for new elements in the new_list.
new_list = []
prev_list = [3,4,5]
print("Before creating list using list comprehension on List : ",new_list)
# new_list = [new_item for item in list]
new_list = [i*2 for i in prev_list]
print("After creating list using list comprehension on List  : ",new_list)
print()

#List Comprehension on String.
language = "Python"
print("Before creating list using list comprehension on String  : ",new_list)
new_list = [letter for letter in language]
print("After creating list using list comprehension on String  : ",new_list)
print()

#List Comprehnesion can be implemented on Python sequences : List, Range, String and Tuple 

