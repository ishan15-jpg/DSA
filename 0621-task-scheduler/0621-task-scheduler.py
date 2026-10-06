class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        pq = []
        freq = {}
        for t in tasks:
            freq[t] = 1 + freq.get(t,0)
        for k,v in freq.items():
            heapq.heappush(pq,(-1*v,k))
        res = 0
        while pq:
            temp = []
            for i in range(n+1):
                if not pq: break
                freq,job = heapq.heappop(pq)
                temp.append((-freq-1,job))
            for freq,job in temp:
                if freq > 0:
                    heapq.heappush(pq,(-freq,job))
            if not pq:
                res += len(temp)
            else: 
                res += n+1
        return res