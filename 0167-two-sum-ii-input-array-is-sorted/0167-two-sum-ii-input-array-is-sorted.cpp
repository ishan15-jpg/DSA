class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        size_t n = numbers.size();

        function<int(int,int)> findRem = [&](int rem, int i) -> int {
            int l = i, h = n-1;

            while(l <= h){
                int mid = (l + h) >> 1;
                if(numbers[mid] == rem) return mid;
                else if(numbers[mid] < rem) l = mid + 1;
                else h = mid - 1;
            }

            return -1;
        };

        for(int i=0; i<n; i++){
            int rem = target - numbers[i];
            int idx = findRem(rem,i+1);
            if(idx != -1) return {i+1, idx+1};
        }

        return {-1,-1};
    }
};