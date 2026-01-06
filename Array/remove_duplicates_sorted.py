'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Time Complexity: O(n)
Space Complexity: O(1)
'''



class solution:
    def removeDuplicates(self,nums):
        if len(nums) == 0:
            return 0
        
        writePos = 0
        for readPos in range(1, len(nums)):
            if nums[readPos] != nums[writePos]:
                writePos += 1
                nums[writePos] = nums[readPos]
                
        return writePos + 1

obj = solution()
print(obj.removeDuplicates([1,1,2,2,3,4,4,5]))