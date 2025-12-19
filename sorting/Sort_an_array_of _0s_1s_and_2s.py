class Solution:
    def sort1(self, arr):
        n = len(arr)
        start = 0
        mid = 0
        end = n - 1

        while mid <= end:
            if arr[mid] == 0:
                arr[start],arr[mid] = arr[mid], arr[start]
                start = start + 1
                mid = mid + 1
            elif arr[mid] == 1:
                mid = mid + 1
            else:
                arr[mid],arr[end] = arr[end], arr[mid]
                end = end - 1
        return arr


solution = Solution()
arr = [0, 1, 2, 0, 1, 2]
print(solution.sort1(arr))  # Output: [0, 0, 1, 1, 2, 2]