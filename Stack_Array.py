#Implementation of stack with an array

from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)

    return stack.pop()

