class Solution:
    def sumOfSquare(self, n: int) -> int:
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n //= 10
        return sum

    def isHappy(self, n: int) -> bool:
        sum = 0
        seen = set()
        while sum != 1:
            sum = self.sumOfSquare(n)
            if sum == 1: return True
            if sum in seen: break
            seen.add(sum)
            n = sum
        return False