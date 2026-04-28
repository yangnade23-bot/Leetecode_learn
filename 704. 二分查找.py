"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。

你必须编写一个具有 O(log n) 时间复杂度的算法
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = (left + right) // 2
        while left < right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            
            mid = (left + right) // 2
        return -1
    