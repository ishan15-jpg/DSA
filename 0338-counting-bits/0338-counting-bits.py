class Solution:
    def countBits(self, n: int) -> List[int]:
        def help(n: int) -> int:
            cnt = 0
            for i in range(0,32): 
                if (n >> i) & 1: cnt += 1
            return cnt
        answer = [ help(i) for i in range(0,n+1) ]
        return answer