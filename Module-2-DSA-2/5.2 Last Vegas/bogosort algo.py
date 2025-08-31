import random

def is_sorted(arr):
    """Check if the array is sorted."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogosort(arr):
    """Sort the array using the Bogosort algorithm."""
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    print(f"Array sorted after {attempts} shuffles.")
    return arr

# Example usage:
array = [3, 2, 5, 1, 4]
print("Unsorted array:", array)
sorted_array = bogosort(array)
print("Sorted array:", sorted_array)

print(""))