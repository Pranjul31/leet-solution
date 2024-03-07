class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for i in range(0,len(nums)):
            if nums[i]==val:
                l+=1
            else:
                nums[i-l]=nums[i]
        return len(nums)-l

        
