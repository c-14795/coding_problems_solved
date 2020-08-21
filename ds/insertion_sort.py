"""
Insertion sort code
values: list of integers
"""


def insertion_sort(values):
    # iterate over the values from 1st index to n-1 index
    # we are assuming that the 0th element is already sorted.
    for unsorted_index in range(1, len(values)):
        # take the first value in the unsorted portion and assign it to element.
        element = values[unsorted_index]

        # In an attempt to move the element from unsorted portion to sorted portion
        # we will assign the current unsorted index to sorted index
        sorted_index = unsorted_index

        # as we assumed sorted index started from zero
        # we will try to fit in the element in the sorted index,
        # until we find the right place for the element we will be looping over it
        # as we loop we move the values in the sorted index towards the right, to make room for new element
        while sorted_index > 0 and values[sorted_index - 1] > element:
            values[sorted_index] = values[sorted_index - 1]
            sorted_index = sorted_index - 1

        # once we find the place we will quit the loop,
        #  insert the element in it's sorted position
        values[sorted_index] = element


if __name__ == "__main__":
    arr = [9, 4, 6, 8, 0]
    insertion_sort(arr)
    print(arr)
