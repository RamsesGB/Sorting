# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a_index = 0
    b_index = 0
    for i in range(0, elements):
        if a_index >= len(arrA):
            merged_arr[i] = arrB[b_index]
            b_index += 1
        elif b_index >= len(arrB):
            merged_arr[i] = arrA[a_index]
            a_index += 1
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
        else: # arrA[a_index] >= arrB[b_index]
            merged_arr[i] = arrB[b_index]
            b_index += 1
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    else:
        left_half = arr[0 : len(arr) // 2]
        right_half = arr[len(arr) // 2 : ]
        left_sorted = merge_sort(left_half)
        right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
