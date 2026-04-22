

"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""
class Solution:
    # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        my_set = set()
        max_len = 0
        while right < len(s):
            if s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            else:
                my_set.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1
        return max_len
