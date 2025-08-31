def makeSortedArray():
    
    array = input("Please enter your sorted array as comma separated numbers: ")
    
    sorted = list(array.split(","))
    
    sorted = [int(x) for x in sorted]
    
    return sorted
    

print(makeSortedArray())