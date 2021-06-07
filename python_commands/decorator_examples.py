# Syntax and what decoration accomplishes:
print("An example where subtract3 is decoratored with add1 and add2 so that the decorated function is the identity.")
def add1(f):
    def wrapper(x):
        return f(x) + 1
    return wrapper

def add2(f):
    def wrapper(x):
        return f(x) + 2
    return wrapper

@add2
@add1
def subtract3(x):
    return x - 3

print(subtract3(5))

print("Allow an argument in the decorator: \n")
print("Here is an example that writes the result of a function with one arg to a text file.\n")

def factorial(n: int) -> int:
    if type(n) == int and n >= 0:
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    else:
        return f"n must be non-negative, you entered {n}"


print("Call the factorial function on -1 and 3\n")
res = factorial(-1)
print(res)
res = factorial(3)
print(res)


# the decorator must be wrapped in a function that accepts the arg and returns the decorator
def logging(file_name):
    def write_log(fn):
        def wrapper(x):
            res = fn(x)
            with open(file_name, "w") as file:
                print(res, file=file)
            return res
        return wrapper
    return write_log

print("Call the factorial function wrapped with 'write_log' and with output.txt as the filename.")

@logging("output.txt")
def factorial(n: int) -> int:
    if type(n) == int and n >= 0:
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    else:
        return f"n must be non-negative, you entered {n}"

res = factorial(3)
print(res)


print("Perpetuate useful attributes of the decorated function:")

def tinsel(fn):
    def wrapper():
        print("tinsel")
        fn()
        print("tinsel")
    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    return wrapper

@tinsel
def tree():
    """This function prints the word 'tree'."""
    print("tree")

tree()
print("tree.__name__ is still", tree.__name__)
print("tree.__doc__ is ", tree.__doc__)

# But this is better accomplished using functools:
from functools import wraps

def tinsel(fn):
    @wraps(fn)
    def wrapper():
        print("tinsel")
        fn()
        print("tinsel")
    return wrapper

@tinsel
def tree():
    """This function prints the word 'tree'."""
    print("tree")

tree()
print("tree.__name__ is still", tree.__name__)
print("tree.__doc__ is ", tree.__doc__)


print("Allow arbitrary args and kwargs")

# See decorate_with_weights.py



# Creating decorator behavior without decorators
def decorate_with(func):
    def wrapper():
        print("Thus it begins...")
        func()
        print("And so it was.")
    return wrapper

def f():
    print("Am I in the middle?")

print("decorate by hand calling \n rapt = decorate_with(f)")
rapt = decorate_with(f)
rapt()

print("now decorate with the @")

@decorate_with
def g():
    print("Am I in the middle?")

g()



print("\n Decorator modifying an argument \n")
def formal(f):
    def wrapper(name):
        name = "Mrs." + name
        ret = f(name)
        return ret
    return wrapper

@formal
def hello(name):
    print(f"hello {name}")

hello("you")

print("\n example from hackerrank \n")

import re
p = re.compile(r"(?:\+91|91|0|)([0-9]{10})")
def wrapper(f):
    def fun(l):
        l_norm = []
        while l:
            phone = l.pop(0)
            if len(phone) == 10:
                phone = "+91 " + phone[:5] + " " + phone[5:]
                l_norm.append(phone)
            else:
                m = p.match(phone)
                phone = m.group(1)
                phone = "+91 " + phone[:5] + " " + phone[5:]
                l_norm.append(phone)
        l = l_norm
        # print("l: ",l)
        return f(l)
    return fun

# @wrapper
# def sort_phone(l):
#     print(*sorted(l), sep='\n')

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


l = ["07895462130","919875641230","9195969878"]
sort_phone(l) 

print("\n Hacker Rank Example \n")

import operator
def person_lister(f):
    def inner(people):
        people.sort(key = operator.itemgetter(2))
        people = [f(person) for person in people]
        return people
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


people = ["Mike Thomson 20 M","Robert Bustle 32 M","Andria Bustle 30 F"]
people = [person.split(" ") for person in people]
print(*name_format(people), sep='\n')
