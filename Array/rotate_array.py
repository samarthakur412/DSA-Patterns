from typing import List

class solution:
    def rotate(self, nums:List[int], k:int)->None:
        n = len(nums)
        k = k%n
        
        self._reverse(nums, 0, n-1)
        self._reverse(nums, 0, k-1)
        self._reverse(nums, k, n-1)
        
    def _reverse(self, nums:List[int], start:int, end:int)->None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -=1

obj = solution()
arr = [1,2,3,4,5,6,7]
print("original array:", arr)
obj.rotate(arr,3)
print("rotated array:", arr)