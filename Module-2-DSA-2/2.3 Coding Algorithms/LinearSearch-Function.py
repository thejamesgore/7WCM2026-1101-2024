def LinearSearch(numbers, target):

    numFound = False

    for i in range (0,len(numbers)):

        if numbers[i]==target:
            numFound = True

            
    if numFound == True:    
        print("I found the number "+str(target)+" in the index "+str(i)+ " of the array.")
    else:
        print("Number not found")
