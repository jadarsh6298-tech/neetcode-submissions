class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        seen = set()
        for i in range(len(s)) :
            while s[i] in seen :
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            curr_len = i - l + 1
            max_len = max(max_len, curr_len)
        return max_len