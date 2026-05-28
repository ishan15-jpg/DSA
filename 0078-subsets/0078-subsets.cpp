class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        size_t n = nums.size();

        vector<vector<int>> answer = {{}};

        for(const int num : nums){
            int size = answer.size();
            for(int i=0; i<size; i++){
                vector<int> temp = answer[i];
                temp.push_back(num);
                answer.push_back(temp);
            }
        }

        return answer;
    }
};