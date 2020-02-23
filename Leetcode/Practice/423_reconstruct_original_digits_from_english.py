from collections import defaultdict


class Solution:
    """Given a non-empty string containing an out-of-order English
     representation of digits 0-9, output the digits in ascending order.
     Preconditions:
     - Only lowercase inputs
     - input is valid
     - Input length is less than 5000
     >>> s = Solution()
     >>> s.originalDigits("owoztneoer")
     '012'
     >>> s.originalDigits("fviefuro")
     '45'
    """

    def originalDigits(self, s: str) -> str:
        numbers = ["zero", "one", "two", "three", "four", "five", "six",
                   "seven", "eight", "nine"]
        number_counts = defaultdict()
        output = ""
        # find zeros
        number_counts['zero'] = s.count("z")
        # find twos
        number_counts['two'] = s.count('w')
        # find fours
        number_counts['four'] = s.count('u')
        # find sixes
        number_counts['six'] = s.count('x')
        # find eights
        number_counts['eight'] = s.count('g')
        # find seven
        number_counts['seven'] = s.count('s') - number_counts['six']
        # find five
        number_counts['five'] = s.count('v') - number_counts['seven']
        # find one
        number_counts['one'] = s.count('o') - number_counts['zero'] - \
                               number_counts['two'] - number_counts['four']
        # find three
        number_counts['three'] = s.count('h') - number_counts['eight']
        # find nine
        number_counts['nine'] = s.count('i') - number_counts['five'] - \
                                number_counts['six'] - number_counts['eight']
        for i, number in enumerate(numbers):
            output += number_counts[number] * str(i)

        return output
