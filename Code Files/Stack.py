# CREATE Stack
def createStack():
    stack = []
    return stack

# EMPTY Stack - check if the stack is empty
def isEmpty(stack):
    return len(stack) == 0

# PUSH Operation
def push_item(stack, item):
    stack.append(item)
    print("Pushed item in the stack : " + item)

# POP Operation
def pop_item(stack):
    return stack.pop()

# PEEK Operation - display the topmost element in the stack
def peek(stack):
    topElement = len(stack)-1
    return str(stack[topElement])

stack = createStack()
while(1):
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    choice = int(input("Enter your choice ? : "))

    if choice == 1:
        val = int(input("Enter the value to be pushed ? : "))
        push_item(stack, str(val))
        print("Current Stack : " + str(stack) + '\n')
    elif choice == 2:
        if isEmpty(stack):
            print("Stack is already empty ! \n")
        else:
            print("Popped Item : " + pop_item(stack))
            print("Current Stack : " + str(stack) + '\n')
    elif choice == 3:
        print("Peek Value : " + peek(stack))
    else:
        exit()
