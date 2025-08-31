# Merge sort algorithm

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid_index = len(arr) // 2
    left_arr = merge_sort(arr[:mid_index])  
    right_arr = merge_sort(arr[mid_index:]) 
    
    return merge_arrays(left_arr, right_arr)

def merge_arrays(left_arr, right_arr):
    merged_arr = []
    
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] <= right_arr[0]:
            merged_arr.append(left_arr.pop(0))  
        else:
            merged_arr.append(right_arr.pop(0))
    
    merged_arr.extend(left_arr)
    merged_arr.extend(right_arr)
    
    return merged_arr

my_array = [222, 1, 4, 3, 2, 5, 9, 7]
print("Here is the sorted array:", merge_sort(my_array))
