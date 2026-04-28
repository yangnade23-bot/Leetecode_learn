from typing import List


"""

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
并返回其长度。如果不存在符合条件的子数组，返回 0 。

"""
class Solution1:
    # 暴力破解
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n + 1
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum >= target:
                    min_len = min(min_len, j - i + 1)
                    break
        return min_len if min_len!=n+1 else 0

        
class Solution2:
    # 滑动窗口
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        slow = 0
        fast = 0
        sum = 0
        min_ken = float('inf') 
        while fast < len(nums):
            sum += nums[fast]
            while sum >= target:
                min_len = min(min_len, fast - slow + 1)
                sum -= nums[slow]
                slow += 1
            fast += 1
        return min_len if min_len != float('inf') else 0