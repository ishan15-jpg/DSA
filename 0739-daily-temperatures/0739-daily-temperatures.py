class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st,answer = list(), [0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                prev_day = st.pop()
                answer[prev_day] = i - prev_day

            st.append(i)

        return answer