class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        for i in range(n // 2):
            temp = arr[i]
            arr[i] = arr[n - i - 1]
            arr[n - i - 1] = temp
        return arr
    
    def reverseArraySimple(self, arr):
        return arr.reverse()

solution = Solution()
arr = [1, 2, 3, 4, 5]
s1 = solution.reverseArray(arr)
s2 = solution.reverseArraySimple(arr)
print(*s1)
print(s2)