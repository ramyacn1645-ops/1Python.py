# adding element to a list
list = [1,2,34,abc,4]
list.append(55)
print(list)

# removing a element from a list
list =[2,3,33,44]
list.remove() # it removes the last element
print(list)
# removing element from a list using poo operator 
list=[1,2,3,4,5]
list.pop() # removes the last element 
print(list)
list.pop(3) # removes the element in the index 3
print(list)

# copying the elements in the list to a another list
list1 =[ 1,2,3,4,5]
list2 = list1.copy() # it just copy the elements in the list

id(list1)l
print(list1)
id(list2)
# ID's are different for both the lists as the 2nd list only copy the elements of 1st list
print(list2) 

# copying the elements in the list to a another list using assignment operator
list1 =[ 1,2,3,4,5]
list2 = list1 # it copy the entire list1 i.e., it also points to the same memory location

id(list1)l
print(list1)
id(list2)
# ID's  of both the lists are same as the list2 copy tne list1 itself not just their elements 
print(list2) 
