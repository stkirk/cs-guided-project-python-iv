# when the variable num is created, it is effectivley a shortcut to the "box" of memory the value is stored in
# num "points" to the address of the memory box
# creates new data
num = 1
# num2 creates another reference pointer to the box that contains the value for num
# doesn't create new data
num2 = num
print("num and num2 are the same object in memory?", num is num2)

num = 2
# creates new data
# numbers are immutable (strings, booleans are similar in this way), so when num is reassigned to 2, the original box it referenced that contained 1 is not modified or destroyed. MEANING - num2 still points to the box in memory that contains the integer 1
print("changed num, num 2 stays the same", num2)

# when num2 is reassigned it first performs the arithmatic to get the value then ceases to point to the value 2 that was instantiated above and now points to the value 3
num2 = num2 + num
# the value 2, which was pointed to by num2 before reassignment now doesn't have any variable that points to its address in memory. Since no variable can reference it, python uses a process called "garbage collection" to get rid of the outdated data that is inaccessible

# MUTABLE
array_1 = [1, 2, 3, 4]
array_2 = array_1
print("array_1 is array_2?", array_1 is array_2) #True
array_1.append(10)
# since arrays are mutable, array_1 is changed in its original address and array_2 still points to that address
# If this wasn't the case it would make changing an array in any way an O(n) operation which is inefficient
# It's more expensive to make a copy and move an array than a number or string
print('array_2 after appending to array 1', array_2)

array_1 = ['a', 'b', 'c', 'd']
# this does not mutate the original array but creates a whole new one, at the same time array_2 is still pointing at the original address that contains the original value
print("array_2 after re-assigning array_1", array_2)
# Same logic applies to all other advanced data types
