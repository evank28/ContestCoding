from typing import List
from collections import defaultdict


# noinspection PyMethodMayBeStatic
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        Given an integer array `arr` and an integer `difference`, return the
        length of the longest subsequence in `arr` which is an arithmetic
        sequence such that the difference between adjacent elements in the
        subsequence equals `difference`.

        >>> s = Solution()
        >>> s.longestSubsequence([1,2,3,4], 1)
        4
        >>> s.longestSubsequence([1,3,5,7], 1)
        1
        >>> s.longestSubsequence([1,5,7,8,5,3,4,2,1], -2)
        4
        >>> s.longestSubsequence([1,2,3,1,2,3,4], 1)
        4
        """
        # Dynamic Programming solution
        # size_below  = defaultdict(int)
        # for num in arr:
        #     size_below[num] = 1 + size_below[num - difference]
        # return max(size_below.values())

        # The same thing without default dict
        size_below = {}
        for num in arr:
            size_below[num] = 1 if num - difference not in size_below else \
                1 + size_below[num - difference]
        return max(size_below.values())

    # Option 1 - first attempt - TLE'd
    #     max_length = 0
    #     checked_indices = set()
    #     for i in range(len(arr)):
    #         cur_length = 1
    #         if i not in checked_indices:
    #             checked_indices.add(i)
    #         this_sequence = subsequence_per_specs(arr[i], difference)
    #         this_sequence.__next__()
    #         cur_i = i
    #         while cur_i < len(arr):
    #             try:
    #                 cur_i = arr.index(this_sequence.__next__(), cur_i+1)
    #                 cur_length += 1
    #             except ValueError:
    #                 break
    #             if cur_i in checked_indices:
    #                 break
    #         max_length = max(cur_length, max_length)
    #         if max_length > len(arr) - 1 - i:
    #             break
    #     return max_length


# def subsequence_per_specs(starts_at: int, difference: int) -> int:
#     """
#     >>> x = subsequence_per_specs(1,2)
#     >>> x.__next__()
#     1
#     >>> x.__next__()
#     3
#     >>> x.__next__()
#     5
#     """
#     next1 = starts_at
#     while True:
#         yield next1
#         next1 += difference
