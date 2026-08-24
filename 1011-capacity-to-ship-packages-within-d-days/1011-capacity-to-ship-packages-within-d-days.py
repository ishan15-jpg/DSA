class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        
        def linear_search():
            min_, max_ = max(weights), sum(weights)
            res = -1
            for i in range(max_,min_-1,-1):
                capacity, no_of_days, j = i,1,0 
                while j < n:
                    if weights[j] > capacity: 
                        no_of_days += 1
                        capacity = i
                    capacity -= weights[j]
                    j += 1
                if no_of_days <= days: 
                    res = i
            return res

        def binary_search():
            low, high = max(weights), sum(weights)
            while low <= high:
                mid = low + (high - low)//2
                j, no_of_days, capacity = 0, 1, mid
                for weight in weights:
                    if weight > capacity:
                        capacity = mid
                        no_of_days += 1
                    capacity -= weight
                if no_of_days > days: low = mid + 1
                else: high = mid - 1
            return low

        return binary_search()
