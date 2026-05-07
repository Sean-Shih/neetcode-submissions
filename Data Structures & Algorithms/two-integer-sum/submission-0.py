class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return False

        dic = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in dic:
                return [dic[comp], i]
            dic[nums[i]] = i




        