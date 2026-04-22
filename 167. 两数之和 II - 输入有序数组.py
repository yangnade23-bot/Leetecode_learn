from typing import List

"""

给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出
满足相加之和等于目标数 target 的两个数。如果设这两个数分别
是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
你所设计的解决方案必须只使用常量级的额外空间。

"""

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
