#This is an example of a monotonic stack. We maintain a stack of the minimum values at each point in time. When we push a new value, we compare it to the current minimum and push the smaller of the two onto the minstack. When we pop a value, we pop from both stacks to maintain the correct minimum value. The top and getMin functions simply return the top of their respective stacks.


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) < 1:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1],val))
        # print(self.minstack)



    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minstack = self.minstack[:-1]
        # print(self.minstack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]