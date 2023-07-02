class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # check if opening bracket
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            # check if closing bracket
            else:
                if not stack:
                    return False
                # if closing bracket and corresponding opening bracket at top of stack,
                # they are for the same grouping. remove from stack
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]([{}])"))