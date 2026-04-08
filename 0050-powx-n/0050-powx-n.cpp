class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0) return 1;
        if(n == 1) return x;
        if(n < 0){
            if(n == INT_MIN) return (1/x)*myPow(1/x, INT_MAX);
            return myPow(1/x, -n);
        }
        if(n%2 == 1) return x*myPow(x, n-1);
        return myPow(x*x, n/2);
    }
};