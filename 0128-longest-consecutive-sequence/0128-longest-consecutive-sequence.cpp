class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int,int> mp;
        int res = 0;
        for(const int num : nums){
            if(mp.find(num) == mp.end()){
                int left = mp.find(num-1) != mp.end() ? mp[num-1] : 0;
                int right = mp.find(num+1) != mp.end() ? mp[num+1] : 0;
                mp[num] = left + right + 1;
                mp[num - left] = mp[num];
                mp[num + right] = mp[num];
                res = max(res,mp[num]);
            }
        }
        return res;
    }
};