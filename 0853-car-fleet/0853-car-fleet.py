class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        cars = [[p,s] for p,s in zip(position,speed)]
        stack = []

        for p,s in sorted(cars)[::-1]:
            t = (target - p) / s

            if not stack or t > stack[-1]: stack.append(t)

        return len(stack)