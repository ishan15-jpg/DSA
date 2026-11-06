class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            else:
                if len(st) > 0 and ((c == ')' and st[-1] == '(') or (c == ']' and st[-1] == '[') or (c == '}' and st[-1] == '{')):
                    st.pop()
                else:
                    return False
        return not st
            