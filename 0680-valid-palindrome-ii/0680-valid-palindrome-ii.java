class Solution {
    public boolean validPalindrome(String s) {
        int l = 0, r = s.length()-1;

        while(l <= r){
            if(s.charAt(l) == s.charAt(r)){
                ++l; --r;
            }else{
                int l_ = l+1, r_ = r; 
                while(l_ <= r_){
                    if(s.charAt(l_) != s.charAt(r_)) break;
                    ++l_; --r_;
                }
                if(l_ > r_) return true;

                l_ = l; r_ = r-1; 
                while(l_ <= r_){
                    if(s.charAt(l_) != s.charAt(r_)) return false;
                    ++l_; --r_;
                }
                if(l_ > r_) return true;
            }
        }

        return true;
    }
}