#author: Sílvia Moros
#date: August 2020
#This program sorts the words "London", "Canterbury", "York" and "Leicester" by their length (in ascending order) and prints the result out.

import random

# First, we define our input as an array of strings
cities = ["London", "Canterbury", "York", "Leicester"]

def selection_sort_by_length(list):

    # You can also try it with a very long list. Uncomment this line to do so.
    # cities = ['Lancaster', 'Sunderland', 'Wolverhampton', 'Nottingham', 'Oxford', 'Plymouth', 'Salisbury', 'Salford', 'Wakefield', 'Lichfield', 'Wells', 'Preston', 'Brighton and Hove', 'St Albans', 'Kingston upon Hull', 'Chichester', 'Durham', 'Liverpool', 'Bath', 'Bradford', 'Cambridge', 'Ely', 'York', 'Exeter', 'Birmingham', 'Carlisle', 'Portsmouth', 'Chester', 'Ripon', 'Coventry', 'Gloucester', 'Sheffield', 'Winchester', 'Lincoln', 'Canterbury', 'Westminster', 'Newcastle upon Tyne', 'Peterborough', 'Worcester', 'Leeds', 'Norwich', 'Stoke-on-Trent', 'Southampton', 'Bristol', 'Derby', 'Truro', 'Manchester', 'Hereford', 'City of London', 'Leicester']

    # Initialize our result, which will be empty for now
    result = []

    # Initialize our loop variables
    i = 0
    j = 0
    number_of_cities = len(list)  # len() of a list gives you the number of elements in it
                                    # len() of a string will give you the lenght of it
    n = number_of_cities


    number_of_steps = 0


    # Sort using selection sort
    for i in range(0, number_of_cities):
        minimum_length = len(list[0])
        minimum_element = list[0]
        

        for j in range(0, n):
            if (len(list[j]) < minimum_length):
                minimum_length = len(list[j])
                minimum_element = list[j]

            number_of_steps = number_of_steps + 1

        # At the end of the second loop, we will have the shorter element in minimum_element
        # We just need to add it to our results and remove it from our working list

        result.append(minimum_element)
        cities.remove(minimum_element)
        n = n - 1


    print("")
    print("The ordered list is:")
    print(str(result))
    print("The list had " + str(number_of_cities) + " cities and I ordered it in " + str(number_of_steps) + " steps.")



selection_sort_by_length(cities)

print("")
print("")
print("")

random_list = [random.randint(1, 100) for _ in range(10)] 

def selection_sort_numbers(list_of_numbers):

    print("The random list of numbers we're going to sort are: ", random_list)
    print("")

    # we initialise the variables that will help us track the numbers we're looping through
    i = 0
    j = i + 1
    
    # this first while loop traverses the entire list
    while i < len(list_of_numbers):
        
        # this second while loop traverses all numbers to the right of index i
        while j < len(list_of_numbers):

            # we do our comparison and check to see if the number to the right of index i is less than the number at index i
            if list_of_numbers[j] < list_of_numbers[i]:
                
                # we create a temp variable to store the first value then switch swap the values 
                temp_number = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[i]
                list_of_numbers[i] = temp_number  
            
            # we now increment j so we compare the next number and repeat the loop    
            j = j + 1
        
        # now we have done the inner loop we can move to the number at the next position and compare it to all the other numbers
        i = i + 1
        
        # we have to reset j to be on the right of the number we shall be comparing to all other numbers
        j = i + 1
    
    print("Here they are sorted :",list_of_numbers)
    




selection_sort_numbers(random_list)