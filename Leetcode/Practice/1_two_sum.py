from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
       >>> s = Solution()
       >>> s.twoSum(nums = [2, 7, 11, 15], target = 9)
       [0, 1]

        """
        """
        # Solution 1 is O(n^2).
        out = []
        for i, n in enumerate(nums):
            for i1, n1 in enumerate(nums):
                if i1 == i:
                    continue
                elif n + n1 == target:
                    out = [i, i1]
            if out:
                break
        return out
        """
        # Solution 2 is O(n)
        # Converting to a set to use its O(1) __contains__ method
        num_set = set(nums)
        val = 0
        # Find the two values
        for n in num_set:
            # Checks if the composite of n is in num_set
            if target-n in num_set:
                val = n
                break

        # Having found the values, now find them using an O(n) search
        i1 = nums.index(val)
        if i1 <= (i2 := (nums[:i1]+nums[i1+1:]).index(target-val)):
            i2 += 1
        return [i1, i2]
