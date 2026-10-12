func canCompleteCircuit(gas []int, cost []int) int {
    sum_gas,sum_cost := 0,0
    for i := range(len(gas)) {
        sum_gas += gas[i]
        sum_cost += cost[i]
    }
    if sum_gas < sum_cost { return -1 }
    res,tank := 0,0
    for i := range(len(gas)) {
        tank += gas[i]-cost[i]
        if tank < 0 {
            tank = 0
            res = i+1
        }
    } 
    return res
}