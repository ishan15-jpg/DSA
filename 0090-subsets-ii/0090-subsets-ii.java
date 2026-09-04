class Solution {
    private void rec(int i, int n, int[] nums, List<Integer> temp, List<List<Integer>>answer){
        if(i == n){
            if(answer.indexOf(temp) == -1) answer.add(new ArrayList<>(temp));
            return;
        }
        temp.add(nums[i]);
        this.rec(i+1,n,nums,temp,answer);
        temp.removeLast();
        this.rec(i+1,n,nums,temp,answer);
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        this.rec(0,n,nums,temp,answer);
        return answer;
    }
}