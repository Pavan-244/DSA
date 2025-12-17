class Solution:
    def pushZerosToEnd(self, arr):
        count = 0  # index for non-zero elements
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1   # move ONLY when non-zero
        
        return arr   # return the modified array
    

solution = Solution()
arr = [1, 2, 0, 5, 0, 7, 0]
s1 = solution.pushZerosToEnd(arr)
print(*s1)
