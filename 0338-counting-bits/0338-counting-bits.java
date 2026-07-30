class Solution {
    private int help(int num){
        int cnt = 0;
        for(int i=0; i<32; ++i)
        if(((num >> i) & 1) == 1) ++cnt;
        return cnt;
    }

    public int[] countBits(int n) {
        int[] answer = new int[n+1];
        for(int i=0; i<n+1; ++i) answer[i] = this.help(i);
        return answer;
    }
}