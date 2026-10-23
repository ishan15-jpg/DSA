class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        e,s = 0,len(gas)-1
        tank = gas[s] - cost[s]
        while s > e:
            if tank >= 0:
                tank += gas[e] - cost[e]
                e += 1
            else:
                s -= 1
                tank += gas[s] - cost[s]
        return s if tank >= 0 else -1