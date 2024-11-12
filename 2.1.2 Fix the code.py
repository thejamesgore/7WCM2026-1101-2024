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
odd = []


for i in range(0, len(data)):
    
    if data[i] % 2 == 0:
        even.append(data[i])

    else:
        odd.append(data[i])


print("In this list of numbers: " + str(data))

print("The even elements are: " + str(even))

print("The odd elements are: " + str(odd))


""" 

# 4. Classes - Original Code

# Gets the student name by ID

class Student:

   def __init__(self, name, student_id):

        self.name = name

        self.student_id = student_id

 

def find_student_by_id(students, search_id):

    for i in range(0, len(students)):

        if students[i].student_id == search_id:

            return students[i]

 

students = [Student("Alice", 42), Student("Bob", 87)]

 

search_ids = [42, 5, 87]

for i in range(0, len(search_ids)):

    student = find_student_by_id(students, search_ids[i])

    print("The student with id " + str(search_ids[i]) + " is " + student.name)

"""

# Gets the student name by ID

# Classes
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

def find_student_by_id(students, search_id):
    for student in students:
        if student.student_id == search_id:
            return student
    return None

# Variables
students = [Student("Alice", 42), Student("Bob", 87)]
search_ids = [42, 5, 87]

for search_id in search_ids:
    student = find_student_by_id(students, search_id)
    if student is not None:
        print("The student with id " + str(search_id) + " is " + student.name)
    else:
        print("No student found with id " + str(search_id))


""" 
# 5. Multiple errors - Original Code:

# Adds the first n numbers

n = input("Please enter a number: ")

 

while i < n

    total = total + i

 

print("The total of the first " + n + " numbers is " + total)

"""


# Adds the first n numbers

n = input("Please enter a number: ")
total = 0

for i in range(int(n)):
    total = total + (int(n)^int(i))
    i = i + 1

print("The total of the first " + str(n) + " numbers is " + str(total))