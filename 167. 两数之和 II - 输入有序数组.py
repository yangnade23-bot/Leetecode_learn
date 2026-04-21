from typing import List

class Solution:
    # 传统解法
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}
        for i, item in enumerate(numbers):
            other=target-item
            if other in cache:
                return [cache[other]+1, i+1]
            cache[item] = i

class Solution2:
    # 双指针
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while not l == r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
