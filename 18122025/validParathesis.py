class Solution:
    def isValidParenthesis(self, s: str)-> int:
        openCount = 0
        validPairs = 0
        for ch in s:
            if ch == "(":
                openCount += 1
            elif ch == ")":
                if openCount > 0:
                    validPairs += 1
                    openCount -= 1
        return validPairs

solution = Solution()
print(solution.isValidParenthesis("()()"))  # Output: 2