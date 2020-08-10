# Sample code to read input and write output:

'''
NAME = input()                # Read input from STDIN
print("Hello " + NAME)        # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted
# data to output will cause the test cases to fail

# Write your code here

numbers_in = str(input())


# def get_valid_combos(word: str) -> int:
#     double_dig_ok = 0
#     for i in range(len(word)-1):
#         if int(word[i]) != 0 and 0 <= int(word[i:i+2]) < 26:
#             double_dig_ok += 1
#         i += 1
#     return 2 ** double_dig_ok

# def count_valid_two_digit_entries(word: str) -> int:
#     # base cases
#     if len(word) == 1:
#         return 0
#     else:
#         cur_two = word[:2]
#         valid = 0
#         if int(cur_two[0]) != 0 and 0 <= int(cur_two) < 26:
#             valid = 1
#             return valid + max(count_valid_two_digit_entries(word[1:]),
#                                count_valid_two_digit_entries(word[2:]))
#         else:
#             return count_valid_two_digit_entries(word[1:])
#
#
# def get_valid_combos(word: str):
#     return 2 ** count_valid_two_digit_entries(word)

# def get_valid_combos(word: str) -> int:
#     # base cases
#     if len(word) == 1:
#         return 1
#     else:
#         cur_two = word[:2]
#         if int(cur_two[0]) != 0 and 0 <= int(cur_two) < 26:
#             if len(word) > 2 and int(cur_two[1]) != 0 and 0 <= int(word[1:3]) < 26:
#                 return 2 * get_valid_combos(word[1:]) * get_valid_combos(word[2:])
#             return 2 * get_valid_combos(word[2:])
#         else:
#             return get_valid_combos(word[1:])

# def get_valid_combos(word: str) -> int:
#     # base cases
#     if len(word) == 1:
#         return 1
#     else:
#         cur_two = word[:2]
#         if int(cur_two[0]) != 0 and 0 <= int(cur_two) < 26:
#             return get_valid_combos(word[1:]) + get_valid_combos(word[2:])
#         else:
#             return get_valid_combos(word[1:])


def generate_combos(word: str) -> list:
    if len(word) == 1:
        return [(int(word), )]
    else:
        combos = []
        cur_two = word[:2]
        if int(cur_two[0]) != 0 and 0 <= int(cur_two) < 26:
            below_double = generate_combos(word[2:])
            for combo in below_double:
                combos.append((int(word[:2]), ) + combo)
        below_single = generate_combos(word[1:])
        for combo in below_single:
            combos.append((int(word[0]), ) + combo)

        return combos


# 100200300
def get_valid_combos(word: str) -> int:
    # base cases
    combos = generate_combos(word)
    return len(set(combos))


print(get_valid_combos(numbers_in))
