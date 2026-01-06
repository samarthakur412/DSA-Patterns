from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # Swap numbers to their correct positions
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target = nums[i] - 1
                nums[target], nums[i] = nums[i], nums[target]

        # Determine the first missing positive number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1  # If all numbers 1 to n are present, return n+1
    
obj = Solution()

print("first missing positive: ",obj.firstMissingPositive([3,4,-1,1]))