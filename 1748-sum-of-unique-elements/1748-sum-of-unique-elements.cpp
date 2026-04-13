class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        size_t n = nums.size();

        int freq[101] = {0};
        int sum = 0;

        for(const int num : nums){
            if(freq[num] == 0){
                sum += num;
                freq[num]++;
            }else{
                if(freq[num] == 1) sum -= num;
                freq[num]++;
            }
        }

        return sum;
    }
};