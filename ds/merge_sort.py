"""
merge sort code
"""


def merge_sort(values):
    print(values, len(values), "called")
    if len(values) > 1:
        # splitting the array into 2 halves
        mid = len(values) // 2
        left_half = values[:mid]
        right_half = values[mid:]

        # recursive call to same function, for the left half of the array
        print('started for left half', left_half)
        merge_sort(left_half)
        # recursive call to same function, for the right half of the array
        print('started for right half', right_half)
        merge_sort(right_half)
        # as the length of array reaches 1, the below code starts executing.
        print('started sorting l:', left_half, 'r:', right_half)
        left_index = right_index = index = 0

        # traverse through the left half and right half
        # alter the values in the array
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                values[index] = left_half[left_index]
                left_index += 1
            else:
                values[index] = right_half[right_index]
                right_index += 1
            index += 1

        # if any elements left in the array  add them to the final array.
        while left_index < len(left_half):
            values[index] = left_half[left_index]
            left_index += 1
            index += 1
        # if any elements left in the array  add them to the final array.
        while right_index < len(right_half):
            values[index] = right_half[right_index]
            right_index += 1
            index += 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 7, 0, 6]
    print(merge_sort(arr))
    print(arr)
