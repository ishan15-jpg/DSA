function missingNumber(nums: number[]): number {
    const n: number = nums.length;
    let [sum, numsSum] = [0,0];

    for(let i=0; i<n+1; i++){
        sum += i;
        if(i < n) numsSum += nums[i];
    }

    return sum-numsSum;
};