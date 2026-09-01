class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        seen = {'{': '}', '[': ']', '(': ')'}

        for i in s:
            if i in seen:
                stack.append(i)
            else:
                if not stack:
                    return False

                if seen[stack[-1]] != i:
                    return False

                stack.pop()

        return not stack