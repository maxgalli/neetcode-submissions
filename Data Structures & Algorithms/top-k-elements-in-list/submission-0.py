class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for n in nums:
            if n not in dct:
                dct[n] = 0
            dct[n] += 1
        return sorted(dct, key=dct.get, reverse=True)[:k]