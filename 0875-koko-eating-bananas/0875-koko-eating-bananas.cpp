class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        size_t n = piles.size();
        int low = 1, high = piles[max_element(piles.begin(),piles.end()) - piles.begin()];

        while(low <= high){
            int mid = (high - low) / 2 + low;
            long time = 0;
            for(int i=0; i<n; ++i){
                time += ceil((double)piles[i] / mid);
            }
            if(time <= h) high = mid - 1;
            else low = mid + 1;
        }

        return low;
    }
};