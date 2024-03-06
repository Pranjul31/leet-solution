class Solution:
    def twoSum(self, nums, target):
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in mp and i != mp[target - nums[i]]:
                return [i, mp[target - nums[i]]]
        return []
