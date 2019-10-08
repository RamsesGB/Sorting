# TO-DO: Complete the selection_sort() function below 
l = [12,4,15,3,7,2,1,14,6]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        #assign the smallest number (at first this will point to the first unsorted element in the list aka index 0)
        index_of_smallest_num = i
        # TO-DO: find next smallest element
        # Note that j starts 1 index ahead of the parent loop
        for j in range(i+1, len(arr)):
            if arr[index_of_smallest_num] > arr[j]:
                '''Upon finding the smallest unsorted number, reassign the value of 
                index_of_smallest_num to the new position (index) at which the smallest 
                number in the array is found'''
                index_of_smallest_num = j

        temp = arr[i]
        arr[i] = arr[index_of_smallest_num]
        arr[index_of_smallest_num] = temp

    return arr

print(selection_sort(l))



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #loops through every element of the given array
    for i in range(0, len(arr) -1):
        #loops through the array and swaps the value on the left for
        #the value on the right if the value on the right is bigger
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


##################################################
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr