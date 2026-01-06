'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

time complexity : O(n)
space complexity : O(1)
'''





class solution:
    def moveZeros(self,nums):
        writePos = 0
        for readPos in range(len(nums)):
            if nums[readPos] !=0:
                nums[writePos], nums[readPos] = nums[readPos], nums[writePos]
                writePos +=1
        return nums
    
obj = solution()
print(obj.moveZeros([0,1,0,3,12]))
