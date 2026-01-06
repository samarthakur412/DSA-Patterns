'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
4. Boyer-Moore Voting Algorithm
Intuition:
The Boyer-Moore Voting Algorithm efficiently finds the majority element in linear time.

It maintains:

candidate: current guess for the majority
count: confidence in the candidate
As you scan:

If count == 0, adopt the current number as the new candidate.
If the current number equals candidate, increment count; otherwise, decrement it.
If a true majority exists, this process guarantees the final candidate is that majority.

time complexity : O(n)
space complexity : O(1)
'''

class solution:
    def majorityElement(self, nums):
        candidate = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count +=1
            else:
                count -=1
        return candidate
    
obj = solution()
print(obj.majorityElement([2, 2, 1, 1, 1, 2, 2, 2]))