class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n <= 0) return false;
        if(n == 1) return true;

        while(n > 0){
            if(n == 1) break;
            if(n%4 > 0) return false;
            n /= 4;
        } 

        return true;
    }
};