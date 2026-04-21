from typing import List
class Solution1:
    # 暴力破解
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, item in enumerate(nums):
            for j in range(i+1, len(nums)):
                post=nums[j]
                if item+post == target:
                    return [i,j]

class Solution2:
    # 哈希表
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ache = {}
        for i, item in enumerate(nums):
            ache[item] = i
        
        for i, item in enumerate(nums):
            other = target - item
            if other in ache and ache[other] != i: # 避免重复
                return [i, ache[other]]


class Solution3:
    # 一次遍历哈希表
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ache = {}
        for i, item in enumerate(nums):
            other = target - item
            if other in ache:
                return [ache[other], i]
            ache[item] = i
