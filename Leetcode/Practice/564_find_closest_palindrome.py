class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        Given an integer n, find the closest integer (not including itself),
        which is a palindrome.
        The 'closest' is defined as absolute difference minimized between two
         integers.
        >>> s = Solution()
        >>> s.nearestPalindromic("123")
        '121'
        >>> s.nearestPalindromic("153999")
        '154451'
        >>> s.nearestPalindromic("1563")
        '1551'
        >>> s.nearestPalindromic("11011")
        '11111'
        """
        if int(n) == 0:
            return 1
        if len(n) <= 1:
            return str(int(n)-1)
        if n[0] == "1" and n[1:-1] == (len(n)-2) * "0" and n[-1] in ["0", "1"]:
            return (len(n)-1) * "9"
        if n == "9" * len(n):
            return "1" + "0" * (len(n)-1) + "1"
        else:
            half = n[:len(n)//2]
            mid = n[len(n)//2] if len(n) % 2 != 0 else ""
            o1 = half + mid + half[::-1]
            if len(n) % 2 == 0:
                o2 = str(int(half)-1) + mid + str(int(half)-1)[::-1]
                o3 = str(int(half)+1) + mid + str(int(half)+1)[::-1]
            else:
                o2 = '1' if mid == '0' else half + str(int(mid) - 1) + \
                                            half[::-1]
                o3 = half + str(int(mid) + 1) + half[::-1] if mid != "9"\
                    else "1"
            smallest_diff = (o2, abs(int(n) - int(o2)))
            if (diff := abs(int(n) - int(o1))) < smallest_diff[1] and o1 != n:
                smallest_diff = (o1, diff)
            if (diff := abs(int(n) - int(o3))) < smallest_diff[1]:
                smallest_diff = (o3, diff)
            return smallest_diff[0]

