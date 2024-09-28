from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []

sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 19
print(sol.twoSum(nums, target)) # the output will be[8,9] cause if we sum up the vale at 8th and 9th index is equals to 19