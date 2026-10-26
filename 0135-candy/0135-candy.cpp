class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> left(ratings.size(),1);
        vector<int> right(ratings.size(),1);
        for(int i=0; i<ratings.size(); ++i){
            if(i > 0 && ratings[i] > ratings[i-1])
                left[i] = left[i-1] + 1;
            if(i < ratings.size()-1 && ratings[ratings.size()-i-2] > ratings[ratings.size()-i-1])
                right[ratings.size()-i-2] = right[ratings.size()-i-1] + 1;
        }
        int res = 0;
        for(int i=0; i<ratings.size(); ++i) res += max(left[i],right[i]);
        return res;
    }
};