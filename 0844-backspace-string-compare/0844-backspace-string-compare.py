class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []
        for i in range(max(len(s),len(t))):
            if i < len(s):
                if s[i] == '#':
                    if st1: 
                        st1.pop()
                else:
                    st1.append(s[i])
            if i < len(t):
                if t[i] == '#':
                    if st2:
                        st2.pop()
                else:
                    st2.append(t[i])
        return ''.join(st1) == ''.join(st2)