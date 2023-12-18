class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = deque(word1), deque(word2)
        res = ""
        while a and b:
            res += a.popleft()
            res += b.popleft()
        res += "".join(a) + "".join(b)
        return res


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(sum(zip_longest(word1, word2, fillvalue=""), ()))
