class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {}
        for i in range(len(nums)):
            if nums[i] in store:
                for j in store[nums[i]]:
                    if abs(i-j) <= k: return True
                store[nums[i]].append(i)
            else: 
                store.setdefault(nums[i], [i])
        return False