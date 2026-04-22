from typing import List

"""

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和
为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

"""
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
