class Solution {
    public static void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void rec(int i, int n, int[] nums, List<List<Integer>> answer){
        if(i == n){
            List<Integer> curr = new ArrayList<>();
            for(int num : nums) curr.add(num);
            answer.add(new ArrayList<Integer>(curr));
            return;
        }
        for(int j=i; j<n; ++j){
            Solution.swap(nums,i,j);
            rec(i+1,n,nums,answer);
            Solution.swap(nums,i,j);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        int n = nums.length;
        List<List<Integer>> answer = new ArrayList<>();
        this.rec(0,n,nums,answer);
        return answer;
    }
}