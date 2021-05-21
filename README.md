# Data Structures & Algorithms Using Python

### Stack

```
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
```

### Queue

```
class Queue:

    # Queue Initialization
    def __init__(self):
        self.queue = []

    # ENQUEUE - Add an element in the queue
    def enqueue(self, item):
        self.queue.append(item)
        print("Item added to queue ! \n")

    # DEQUEUE - Remove an element from the queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)
    
    # DISPLAY - display the queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty !")
        else:
            print("Current Queue : ",self.queue, '\n')
    
    # SIZE - display the size of the queue
    def size(self):
        return print("Size of queue : ", len(self.queue), '\n')

myQueue = Queue()
while(1):
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. DISPLAY")
    print("4. SIZE")
    choice = int(input("Enter your choice ? : "))
    if choice == 1:
        val = int(input("Enter the value to be added to Queue ? : "))
        myQueue.enqueue(val)
    elif choice == 2:
        myQueue.dequeue()
        print("Item has been popped ! \n")
    elif choice == 3:
        myQueue.display()
    elif choice == 4:
        myQueue.size()
    else:
        exit()
```
