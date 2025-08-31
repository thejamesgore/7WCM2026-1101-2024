# 1 Define two integers, add them together and print the result to the screen

int_1 = 256
int_2 = 111

print(int_1 + int_2)

# 2 Modify the program above so instead of defining the two integers in code, they are asked as an input from the user.

int_3 = input('Input the value of an integer: ')
int_4 = input('Input the value of another integer: ')

sum_of_ints = int_3 + int_4

print('The value of the sum of those two integers is:', sum_of_ints)

# 3 Program the fizzbuzz challenge.

print("Now it's time for the fizz buzz portion of code")
print('  ')
for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz ', i)
    elif i % 3 == 0:
        print('Fizz', i)
    elif i % 5 == 0:
        print('Buzz', i)
    else:
        print(i)
print('  ')

''' 
4 Modify the fruit shopping list program so we can use it for a general shopping list, in the following way:

- The program must ask you if you have all the necessary items in the shopping list
- If no, it should let you add items until you’re happy with it
- If yes, it should show a message showing the items
'''

# 5 Modify the shopping list program so it lets you delete items from the shopping list (you can use the “remove” function).