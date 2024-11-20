# My fibonnaci function build using recursion

def fib_func(n):
    if n == 0 or n == 1:
        return n
    return n + fib_func(n - 1)


print("The fibonacci number is",fib_func(88))