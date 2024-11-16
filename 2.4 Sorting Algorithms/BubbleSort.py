#author: James Gore
#date: November 2024
# This function will sort a list in ascending order. The list can be integers, or words. If words it can sort them either by length or alphabetical order

cities = ["London", "Canterbury", "York", "Leicester", "Antwerp"]


def bubble_sort(list):
    print("Lets do the bubble sort algorithm!!")
    print("   ")
    print("   ")
    print("We're going to sorting the following: ", list)
    
    i = 0
    has_swapped = True
    
    while has_swapped == True:
        has_swapped = False
        for i in range(len(list) -1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                has_swapped = True
        i = 0
        
