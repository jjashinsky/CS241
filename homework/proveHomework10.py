numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]

#1 Insert the number 5 to the beginning of the list.

numbers.insert(0,5)
print(numbers)

#2 Remove the number 2348 based on its value
#  (as opposed to a hard-coded index of 4) from the list.

numbers.remove(2348)

print(numbers)


#3 Create a second list of 5 different numbers
#  and add them to the end of the list in one step.
#  (Make sure it adds the numbers to the list such as: [1, 2, 3, 4, 5]
#  not as a sub list, such as [1, 2, 3, [4, 5]] ).

additional_list = [1,2,3,4,5]
numbers += additional_list
print(numbers)


#4 Sort the list using the built in sorting algorithm.

numbers.sort()
print(numbers)

#5 Sort the list backwards using the built in sorting algorithm.
numbers.sort(reverse = True)
print(numbers)

#6 Use a built-in function to count the number of 12's in
#  the list.

print(numbers.count(12))


#7 Use a built-in function to find the index of the number 96.

print(numbers.index(96))


#8 Use slicing to get the first half of the list, then get
#  the second half of the list and make sure that nothing was
#  left out or duplicated in the middle.

i = len(numbers) // 2
first_half = numbers[:i]
second_half = numbers[i:]
print(first_half)
print(second_half)


#9 Use slicing to create a new list that has every other item
#  from the original list (i.e., skip elements, using the step
#  functionality).


new_list = numbers[:]
print(new_list)

#10 Use slicing to get the last 5 items of the list. For
#   this, please use negative number indexing.

print(new_list[-5:])
