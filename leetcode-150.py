class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = "+-*/"
        stack = deque()
        for i in tokens:
            print(stack)
            if i not in operations:
                stack.append(int(i))

            else:
                t1 = stack.pop()
                t2 = stack.pop()
                if i == "*":
                    stack.append(t1*t2)
                if i == "-":
                    stack.append(t2-t1)
                if i == "+":
                    stack.append(t1+t2)
                if i == "/":
                    stack.append(int(t2/t1))
        return stack.pop()
            