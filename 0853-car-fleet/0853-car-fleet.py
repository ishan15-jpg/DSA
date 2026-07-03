class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(key=lambda x: x[0], reverse=True)
        max_,fleet = -math.inf, 0
        for p,s in pairs:
            time = (target - p) / s
            if time > max_:
                max_ = time
                fleet += 1

        return fleet