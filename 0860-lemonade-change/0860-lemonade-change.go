func lemonadeChange(bills []int) bool {
    change := make(map[int]int)
    change[0] = 0
    change[5] = 0
    change[20] = 0
    for _,bill := range bills {
        if bill == 5 {
            change[5] += 1
        } else if bill == 10 {
            if change[5] >= 1 {
                change[5] -= 1
            } else { return false }
            change[10] += 1
        } else {
            if change[5] >= 1 && change[10] >= 1 {
                change[5] -= 1
                change[10] -= 1
            } else if change[5] >= 3 {
                change[5] -= 3
            } else { return false }
            change[20] += 1
        }
    }
    return true
}