if len(nums)<=1:
            return
        for i in range(0,len(nums)):
            key=nums[i]
            j=i-1
            while j>=0 and key<nums[j]:
                nums[j+1]=nums[j]
                j -= 1
            nums[j+1]=key

# Code By Pranjul Mishra
