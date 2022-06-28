from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for word in strs:
            temp[str(sorted(word))].append(word)
        return list(temp.values())
