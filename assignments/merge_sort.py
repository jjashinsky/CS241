"""
File: ta10-solution.py
Author: Br. Burton
This file demonstrates the merge sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint
MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """

    if len(items) <= 1:
        return
    
    middle = len(items) // 2 
    left = items[:middle]
    right = items[middle:]
        
    merge_sort(left)
    merge_sort(right)
        
    left_index = 0
    right_index = 0
    list_index = 0
        
        
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            items[list_index] = left[left_index]
            left_index += 1
            list_index += 1
        else:
            items[list_index] = right[right_index]
            right_index += 1
            list_index += 1
        
    while left_index < len(left):
        items[list_index] = left[left_index]
        left_index += 1
        list_index += 1
            
    while right_index < len(right):
        items[list_index] = right[right_index]
        right_index += 1
        list_index += 1
    

def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()