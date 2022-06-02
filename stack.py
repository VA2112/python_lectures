class Stack:
    def __init__(self, init_stack=[]):
        self.stack = init_stack

    def count(self):
        return len(self.stack)

    def add(self, el):
        self.stack.append(el)

    def get(self):
        return self.stack.pop(-1)

    def get_k(self, k):
        return self.stack.pop(-k)

    def clear(self):
        self.stack = []

    def print_top(self, n):
        print(*self.stack[-1:-(n+1):-1], sep='\n')

    def __str__(self):
        return '\n'.join([str(el) for el in reversed(self.stack)])

    def __add__(self, other):
        return Stack(self.stack + other.stack)


stack1 = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9])
stack2 = Stack(['a', 'b', 'c', 'd', 'e'])

stack1.print_top(3)
print()
stack2.print_top(3)
print()
print(stack2)
print()

print(stack1.get())
print()
print(stack1.get_k(3))
print()
stack1.add(10)
print(stack1)
print()
print(stack1.count())
print()
print(stack1 + stack2)
