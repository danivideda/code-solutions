class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        val = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in val:
                stack.append(char)
            else:
                if len(stack) and val[stack[-1]] == char:
                    del stack[-1]
                else:
                    return False

        return not stack

s = "(({{}}))"
s = "["
s = "()()[[]]"
print(Solution().isValid(s))
