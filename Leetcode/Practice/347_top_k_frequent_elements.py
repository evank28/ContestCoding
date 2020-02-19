from collections import defaultdict
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given a non-empty array of integers, return the k most frequent
        elements.
        >>> s = Solution()
        >>> s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
        [1, 2]
        >>> s.topKFrequent(nums = [1], k = 1)
        [1]
        """
        frequency_map = defaultdict(int)
        for n in nums:
            frequency_map[n] += 1
        freq_sorted = {k: v for k, v in
                       sorted(frequency_map.items(), key=lambda x: x[1],
                              reverse=True)}
        return list(freq_sorted.keys())[:k]
