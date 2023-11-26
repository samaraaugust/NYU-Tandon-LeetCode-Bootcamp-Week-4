class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr = []

        for c in s:
            if c == '(':
                arr.append(c)
            elif c == ')' and arr and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(c)

        return len(arr)
