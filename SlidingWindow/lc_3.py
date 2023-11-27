# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use dictionary
        seen = {}

        start = 0
        max_length = 0

        for end in range(len(s)):
            char = s[end]
            if char in seen:
                start = max(start, seen[char] + 1)
            seen[char] = end
            max_length = max(max_length, end - start + 1)

        return max_length


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
