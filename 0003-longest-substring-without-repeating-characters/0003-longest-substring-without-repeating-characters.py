class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res,l = 0,0
        st = set()
        for r in range(n):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            r += 1
            res = max(res,r-l)
        return res