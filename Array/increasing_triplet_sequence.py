from typing import List 

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize the first and second variables to the maximum possible value
        first = float('inf')
        second = float('inf')

        # Traverse the array
        for num in nums:
            # If current number is less than or equal to the first, update first
            if num <= first:
                first = num
            # Else if current number is less than or equal to the second, update second
            elif num <= second:
                second = num
            # Else we found a number greater than both first and second
            else:
                return True
        return False
    
obj = Solution()
arr = [1,2,3,4]
print(obj.increasingTriplet(arr))