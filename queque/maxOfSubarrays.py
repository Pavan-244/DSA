from collections import deque

class Solution:
    def max_of_sub_arrays(self, arr, k):
        n = len(arr)
        res = []
        dq = deque()

        for i in range(k):
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        for i in range(k, n):
            res.append(arr[dq[0]])

            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
            
        res.append(arr[dq[0]])
        return res

solution = Solution()
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(solution.max_of_sub_arrays(arr, k))  # Output: [3, 3, 5, 5, 6, 7]