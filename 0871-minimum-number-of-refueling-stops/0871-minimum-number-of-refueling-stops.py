class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        stations.append([target,0])
        pre = 0
        curr = startFuel
        pq = []
        res = 0
        for station in stations:
            pos,fuel = station
            dist = pos-pre
            curr -= dist
            while pq and curr < 0:
                curr -= heapq.heappop(pq)
                res += 1
            if curr < 0:
                return -1
            heapq.heappush(pq,-fuel)
            pre = pos
        return res