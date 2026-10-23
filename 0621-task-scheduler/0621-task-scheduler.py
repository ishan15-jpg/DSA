class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = [0] * 26
        maxF = 0
        for task in tasks:
            idx = ord(task) - ord('A')
            freq[idx] += 1
            maxF = max(maxF,freq[idx])
        freq.sort(reverse=True)
        slots = (maxF - 1) * n
        for i in range(1,26):
            slots -= min(freq[i], maxF-1)
        return len(tasks) if slots < 0 else len(tasks) + slots