class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int n = weights.length;

        int low = Arrays.stream(weights).max().getAsInt();
        int high = Arrays.stream(weights).sum();

        while(low <= high){
            int mid = low + (high - low) / 2;
            int capacity = mid, no_of_days = 1;
            for(int weight : weights){
                if(weight > capacity){
                    ++no_of_days;
                    capacity = mid;
                }
                capacity -= weight;
            }
            if(no_of_days > days) low = mid + 1;
            else high = mid - 1;
        }

        return low;
    }
}