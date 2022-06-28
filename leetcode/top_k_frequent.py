from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rates = dict(Counter(nums))
        sorted_form = dict(
            sorted(rates.items(), key=lambda item: item[1], reverse=True)
        )
        a = list(sorted_form.keys())
        return a[:k]
