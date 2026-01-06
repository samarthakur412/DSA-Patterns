from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        zeroCount = 0
        
        for num in nums:
            # Check if the current number is zero
            if num == 0:
                # Extend the current zero sequence
                zeroCount += 1
            else:
                # Calculate subarrays for the zero sequence
                result += zeroCount * (zeroCount + 1) // 2
                # Reset zero sequence counter
                zeroCount = 0
        
        # If the last element was part of a zero sequence, add its subarrays
        result += zeroCount * (zeroCount + 1) // 2
        
        return result
    
obj = Solution()
print(obj.zeroFilledSubarray([0,0,0,2,0,0]))