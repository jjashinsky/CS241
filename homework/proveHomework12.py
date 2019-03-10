"""
Purpose: This file is a starting point to help you practice using lambda functions.
"""

import functools


def get_part1_list():
    """
    Filters a list to return even numbers greater than 33.
    """
    numbers = [x for x in range(100)]

    # TODO: Write a line here that uses filter and a lambda function to filter
    # the list so that it only contains even numbers greater than 33.
    my_filter = lambda i : i > 33 and i % 2 == 0
    new_numbers = list(filter(my_filter, numbers))


    return new_numbers

def get_part2_list():
    """
    Maps a lambda function to a list to square each number and add one.
    """
    numbers = [x for x in range(100)]

    # TODO: Write a line here than uses map and a lambda function to go through
    # each number in the list, square it and then add one to the result
    square_plus = lambda i : (i ** 2) + 1
    new_numbers = list(map(square_plus, numbers))


    return new_numbers

def get_part3_list():
    """
    Reduces a list to its product
    """
    numbers = [x for x in range(1, 100)]

    # TODO: Write a line here that uses reduce and a lambda function to
    # multiply all the numbers in the list together and return the product
    product = 0
    PI = lambda prev, new : prev * new
    product = functools.reduce(PI, numbers, 1)
    return product

def main():
    """
    This function calls the above functions and displays their result.
    """
    print(get_part1_list())
    print(get_part2_list())
    print(get_part3_list())


if __name__ == "__main__":
    main()