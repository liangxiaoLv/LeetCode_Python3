# Solution 1
# brute force solution  暴力求解
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]+nums[j]==target:
                    return [j,i]

# Solution 2 (better)
# using hashtable 使用哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            else:
                hashtable[nums[i]]=i
        return []

