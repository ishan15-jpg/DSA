class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        res = 0
        people.sort()
        i,j = 0,len(people)-1
        for j in range(len(people)-1,-1,-1): 
            if i > j: break
            if i == j: 
                res += 1
                break
            if people[i] + people[j] <= limit: 
                i += 1
            res += 1
        return res