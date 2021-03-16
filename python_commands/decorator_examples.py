def decorate_with(f, prologue, postlogue):
    def wrapper():
        print(prologue)
        f()
        print(postlogue)
    return wrapper

def f():
    print("Am I in the middle?")

rapt = decorate_with(f, "Thus it begins...", "And so it was.")
rapt()

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
