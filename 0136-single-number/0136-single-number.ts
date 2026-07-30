function singleNumber(nums: number[]): number {
    let temp: number = 0
    nums.forEach(num => { temp ^= num })
    return temp
};