# create a class with class name Solution
# And then create a function in side the class to retrieving the 2nd largest element
# And the funtion take one argument which is arr in this case
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)

        #intialozing the values
        largest = -1
        secondLargest = -1

        # for loop itreating over the array
        for i in range(n):
            #In the first case arr[i] = 12 > -1 then secondLargest = 12 largest = 12
            if arr[i]>largest:
                secondLargest = largest
                largest = arr[i]
            elif arr[i]<largest and  arr[i]>secondLargest:
                secondLargest = arr[i]
        return secondLargest

solution = Solution()
arr = [12, 35, 1, 10, 34, 1]
print(solution.getSecondLargest(arr))