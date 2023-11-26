class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sumVal = [0] * (n + 1)
        for i in range(n):
            sumVal[i + 1] = sumVal[i] + nums[i]

        short = float('inf')
        value = deque()

        for i in range(n + 1):
            while value and sumVal[i] - sumVal[value[0]] >= k:
                short = min(short, i - value.popleft())

            while value and sumVal[i] <= sumVal[value[-1]]:
                value.pop()

            value.append(i)

        return short if short != float('inf') else -1
