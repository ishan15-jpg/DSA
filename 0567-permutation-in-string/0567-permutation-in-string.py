class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2 = len(s1),len(s2)
        if l1 > l2: return False
        count1 = {}
        count2 = {}
        for r in range(l1): 
            count1[s1[r]] = 1 + count1.get(s1[r],0)
            count2[s2[r]] = 1 + count2.get(s2[r],0)
        if count1 == count2: return True
        for r in range(l1,l2):
            count2[s2[r]] = 1 + count2.get(s2[r],0)
            count2[s2[r-l1]] -= 1 
            if count2[s2[r-l1]] == 0: del count2[s2[r-l1]]
            if count2 == count1: return True
        return False