from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {num, index} dictionary
        nums_dict = {}

        for i, num in enumerate(nums):
            index = nums_dict.get(target - num)
            if index != None:
                return [index, i]

            nums_dict[num] = i

        return []

    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]

        return []
