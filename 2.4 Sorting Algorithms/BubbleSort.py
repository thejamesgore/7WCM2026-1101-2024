#author: James Gore
#date: November 2024
# This function will sort a list in ascending order. The list can be integers, or words. If words it can sort them either by length or alphabetical order

cities = ["London", "Canterbury", "York", "Leicester", "Antwerp"]


def bubble_sort_by_length(list):
    print("Lets do the bubble sort algorithm!!")
    print("   ")
    print("   ")
    print("We're going to sort the following: ", list)
    
    i = 0
    has_swapped = True
    
    while has_swapped == True:
        has_swapped = False
        for i in range(len(list) -1):
            # print("DO WE NEED TO SWAP ??", list[i], list[i + 1])
            if len(list[i]) > len(list[i + 1]): # notable issue when comparing final two items in list. If I use < or > then it will incorrectly state that Canterbury is of a shorter length than Antwerp
                list[i], list[i + 1] = list[i + 1], list[i]
                # print("YES, WE JUST DID A SWAP !!", list[i], list[i + 1])
                has_swapped = True
                # print(" Our new list order is --->", list)
            else:
                # print("NO WE DID NOT NEED TO SWAP ...", list[i], list[i + 1])
                # print(" Our new list order is --->", list)
            i = i + 1
        i = 0
        
    print("The newly sorted list is: ", list)

# bubble_sort_by_length(cities)


def bubble_sort_alphabetical(list):
    print("Lets sort alphabetically then!")
    print("   ")
    print("   ")
    print("We're going to sort the following: ", list)
    
    i = 0
    has_swapped = True
    
    while has_swapped == True:
        has_swapped = False
        
        for i in range(len(list) -1):
            left = list[i]
            right = list[i + 1]
            
            if len(left[-1]) < len(right[-1]):
                list[i], list[i + 1] = list[i + 1], list[i]
                has_swapped = True
            i = i + 1
        i = 0
        
    print("The newly sorted list in alphabetical order is :", list)
            
            
bubble_sort_alphabetical(cities)