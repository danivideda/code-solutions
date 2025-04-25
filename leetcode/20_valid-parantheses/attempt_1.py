class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        op = ['[', '{', '(']

        for char in s:
            if char in op:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                match char:
                    case ')':
                        if stack[len(stack) - 1] != '(':
                            return False
                        stack.pop()
                    case '}':
                        if stack[len(stack) - 1] != '{':
                            return False
                        stack.pop()
                    case ']':
                        if stack[len(stack) - 1] != '[':
                            return False
                        stack.pop()

        if len(stack) != 0:
            return False

        return True


s = "(({{}}))"
s = "["
s = "()()[[]]"
print(Solution().isValid(s))
