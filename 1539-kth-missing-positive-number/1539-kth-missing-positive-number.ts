function findKthPositive(arr: number[], k: number): number {
    let [s, e] = [0, arr.length-1];

    while(s <= e){
        const mid: number = Math.floor((s + e)/2);
        if((arr[mid] - mid - 1) < k) s = mid + 1;
        else e = mid - 1;
    }

    return s+k;
};