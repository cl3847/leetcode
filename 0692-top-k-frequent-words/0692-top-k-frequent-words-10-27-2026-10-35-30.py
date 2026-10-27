class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        count = sorted(count, key=lambda x: (-count[x], x))
        return count[:k]