#
#  Fix the errors in the code
#

"""
1. Syntax errors - Original code:

# Reads your name and age

name = input("Enter your name: ")

 age = input("Enter your age": )

 

print("Your name is " + name + " and you are " + age "years old.")

"""

# Reads your name and age

name = input("Enter your name: ")
age = input("Enter your age: " )
print("Your name is " + name + " and you are " + age + " years old.")



""" 
# 2. Unmatched data types - Original Code:

# Shows the first 10 multiples of a number

n = input("Enter a number: ")

 

print("The first 10 multiples of " + n + " are:")

for i in range(1, 11):

    print(str(i) + "x" + n + "= " + i * n)

"""
# Shows the first 10 multiples of a number

n = input("Enter a number: ")

print("The first 10 multiples of " + n + " are:")

for i in range(1, 11):
    print(str(i) + "x" + n + "= ", int(i) * int(n))
    


""" 

# 3. Null reference errors - Original Code:

# Splits a list into even and odd elements

data = [9,4,5,17,12,14,1,0,3,10,9]

even = []

 

for i in range(0, len(data)):

    if data[i] % 2 == 0:

        # Found an even element

        even.append(data[i])

        # Remove element from the list

        data.pop(i)

 

print("The even elements are: " + str(even))

print("The odd elements are: " + str(data))

"""

# Splits a list into even and odd elements

data = [9,4,5,17,12,14,1,0,3,10,9]

even = []

 

for i in range(0, len(data)):

    if data[i] % 2 == 0:

        # Found an even element

        even.append(data[i])

        # Remove element from the list

        data.pop(i)

 

print("The even elements are: " + str(even))

print("The odd elements are: " + str(data))