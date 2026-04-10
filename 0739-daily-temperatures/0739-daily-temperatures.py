class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 1 : return [0]

        st,answer = list(), [0]*n

        for i in range(0,n):
            while len(st) > 0 and temperatures[i] > temperatures[st[-1]]:
                answer[st[-1]] = i - st[-1]
                st.pop(-1)
            st.append(i)

        return answer