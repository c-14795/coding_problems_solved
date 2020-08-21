"""
Quick Sort
"""""


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

def partition(_arr, low, high):
    _i = (low - 1)  # index of smaller element
    pivot = _arr[high]  # pivot

    for j in range(low, high):
        print(_arr[j], pivot, "values before pivot check", _arr)
        # If current element is smaller than the pivot, move it to the left of the array
        if _arr[j] < pivot:
            # increment index of smaller element
            _i = _i + 1
            _arr[_i], _arr[j] = _arr[j], _arr[_i]
        print(_arr[j], pivot, "values after pivot check", _arr)

    # changing the pivot position.
    _arr[_i + 1], _arr[high] = _arr[high], _arr[_i + 1]
    return _i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quick_sort(_arr, low, high):
    print("low:", low, "high:", high, "array", _arr)
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(_arr, low, high)
        print("after partition", _arr, pi)

        # call recursively quick sort
        quick_sort(_arr, low, pi - 1)
        quick_sort(_arr, pi + 1, high)


if __name__ == '__main__':
    arr = [11, 77, 8, 9, 1, 15]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i])
