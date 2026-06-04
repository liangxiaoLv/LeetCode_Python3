class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        flag = 0
        count = 0
        for i in range(len(nums)):
            if (nums[i] == 1 and flag == 0):
                # 进入统计
                flag = 1
                count = 1
                m = max(1, count)
            elif (nums[i] == 0 and flag == 1):
                count = 0
            elif (nums[i] == 1 and flag == 1):
                count += 1
                m = max(m, count)
        return m
