class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mp={}
        for i in range(0,len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
            else:
                mp[nums[i]]=1
        ls=list(mp.values())
        return max(ls)*ls.count(max(ls))

  #daily challenge of = 3:8:24
