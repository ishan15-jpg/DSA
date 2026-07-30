function countBits(n: number): number[] {
    const help = (num: number) => {
        let cnt: number = 0
        for(let i=0; i<32; ++i)
        if((num >> i) & 1) ++cnt
        return cnt
    }
    const answer: Array<number> = []
    for(let i=0; i<n+1; ++i) answer.push(help(i))
    return answer
};