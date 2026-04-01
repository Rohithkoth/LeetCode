class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        left ="({["
        right = ")}]"
        for c in s:
            print(stack)
            if c in left:
                stack.append(c)
            elif(c in right):
                if len(stack) == 0:
                    return False
                elif (c == '}' and stack[-1] == '{') or (c==']' and stack[-1] == '[') or (c==')' and stack[-1] == '('):
                    stack.pop()
                else:
                    stack.append(c)
        print(stack)
        return len(stack) ==0