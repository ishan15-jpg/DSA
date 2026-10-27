class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c)-ord('a')] += 1
        pq = []
        for f in freq:
            if f > 0:
                heapq.heappush(pq,-f)
        res = 0
        while len(pq) > 1:
            a = -1 * heapq.heappop(pq)
            b = -1 * heapq.heappop(pq)
            if a == b: 
                res += 1
                if b-1 > 0:
                    heapq.heappush(pq,-(b-1))
                heapq.heappush(pq,-a)
            else:
                heapq.heappush(pq,-b)
        return res
            