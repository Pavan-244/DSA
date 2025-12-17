class Solution:
    def rotateArray1(self, arr, d):
        #python program to left rotate the array by d positions
        #by rotating one by one

        #length of array
        n = len(arr)

        for i in range(d):
            # i = 0,1,2,...d-1, d=2
            #arr[0] -> first element of array -> 1
            first = arr[0]
            # j = 0,1,2,...n-2 here n = 7 and loop runs from 0 to 6
            for j in range(n-1): 
                # arr[0] = arr[1], arr[1] = arr[2],...,arr[5] = arr[6] 
                arr[j] = arr[j+1]
                # arr[6] = first -> arr[6] = 1 
            arr[n-1] = first 
        return arr 
    
    def rotateArray2():
        pass
    def rotateArray3():
        pass

solution = Solution()
array = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotated_array = solution.rotateArray1(array, d)
print(rotated_array)  # Output: [3, 4, 5, 6, 7, 1, 2]