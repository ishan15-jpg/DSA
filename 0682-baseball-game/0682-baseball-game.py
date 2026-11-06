class Solution:
  def calPoints(self, operations: list[str]) -> int:
    st = []
    for op in operations:
      if op == 'C' or op == 'D' or op == '+':
        if op == 'C':
          st.pop()
        elif op == 'D':
          st.append(st[-1] * 2)
        else:
          st.append(st[-1] + st[-2])
      else:
        st.append(int(op))
    return sum(st)