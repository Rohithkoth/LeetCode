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