class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s,e = 0, len(arr)-1

        while s <= e:
            mid = (s+e)//2
            if arr[mid] - mid - 1 < k: s = mid + 1
            else: e = mid - 1

        return s+k