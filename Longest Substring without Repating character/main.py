class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sett = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            max_length = max(max_length, len(sett))
        return max_length


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    result = sol.lengthOfLongestSubstring(s)
    print("The Length of Longest Substring without repeating characters:", result)
