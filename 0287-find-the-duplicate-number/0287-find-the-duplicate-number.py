class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow,fast = nums[slow],nums[nums[fast]]
            if slow == fast: break
        fast = nums[0]
        while True:
            if slow == fast: break
            slow,fast = nums[slow],nums[fast] 
        return slow