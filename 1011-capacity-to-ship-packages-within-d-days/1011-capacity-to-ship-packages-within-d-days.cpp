class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        size_t n = weights.size();

        int low = *max_element(weights.begin(),weights.end());
        int high = accumulate(weights.begin(),weights.end(),0);

        while(low <= high){
            int mid = low + (high - low) / 2;
            int capacity = mid, no_of_days = 1;
            for(const int weight : weights){
                if(weight > capacity){
                    ++no_of_days;
                    capacity = mid;
                }
                capacity -= weight;
            }
            if(no_of_days > days) low = mid + 1;
            else high = mid - 1;
        }   

        return low;
    }
};