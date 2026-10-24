class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        curr = startFuel
        pre = 0
        ans = 0
        stations.append([target,0])
        pq = []
        for pos,fuel in stations:
            dist = pos - pre
            curr -= dist
            while pq and curr < 0:
                curr -= heapq.heappop(pq)
                ans += 1
            if not pq and curr < 0:
                return -1
            heapq.heappush(pq,-fuel)
            pre = pos
        return ans