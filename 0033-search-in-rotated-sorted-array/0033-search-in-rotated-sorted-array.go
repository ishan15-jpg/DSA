func search(nums []int, target int) int {
    l,r := 0,len(nums)-1
    for l < r {
        mid := (l+r) >> 1
        if nums[mid] > nums[r] {
            l = mid + 1
        } else { r = mid }
    }
    binarySearch := func(l int, r int) int {
        for l <= r {
            mid := (l+r) >> 1
            if nums[mid] == target { 
                return mid 
            } else if nums[mid] < target {
                l = mid+1
            } else { r = mid-1}
        }
        return -1
    }
    if target >= nums[l] && target <= nums[len(nums)-1] { return binarySearch(l,len(nums)-1) }
    return binarySearch(0,l-1)
}