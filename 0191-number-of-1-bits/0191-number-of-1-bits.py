class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(0,32):
            if (n >> i) & 1 == 1: cnt += 1
        return cnt