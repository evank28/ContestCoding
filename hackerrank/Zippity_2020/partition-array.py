
def partitionArray(k:int, numbers: list) -> str:
    """
    >>> partitionArray(2, [1,2,3,4])
    'Yes'
    >>> partitionArray(3, [1,2,2,3])
    'No'
    """
    # Check if it can be partitioned into k-length subsequences
    if len(numbers) % k != 0:
        return 'No'
    else:
        number_of_subs_needed = len(numbers) / k
        uniques = set(numbers)
        mult_objs = 0
        for num in uniques:
            instances = numbers.count(num)
            if instances > 1 and instances > mult_objs:
                mult_objs = instances
        if mult_objs <= number_of_subs_needed:
            return 'Yes'
        return 'No'

# def get_subsequence(k: int, numbers:list)
#     if len(numbers) == k:
#         return numbers
#     else:
#
# def list_of_partitions(k:int, numbers: list)
#     for index in range(len(numbers)):
#         pick = index
#

# def list_of_partitions(k:int, numbers: list)
#     partitions = []
#     first_picks = subsequences_of_length_k(k, numbers)
#     for start_seq in first_picks:
#         for _ in range(k - 2):
#             i = 0
#             indices_to_remove = []
#             for k, num in enumerate(numbers):
#                 if num == start_seq[i]:
#                     indices_to_remove.append(i)
#
#
#
#
# def subsequences_of_length_k(k: int, sequence: list) -> list:
#     """
#     Precondition: k >= 1
#     """
#     if k == 1:
#         return [[x] for x in sequence]
#     else:
#         subsequences = []
#         for start in range(len(sequence)):
#             first_element = sequence[start]
#             after = subsequences_of_length_k(k - 1, sequence[start + 1:])
#             for seq in after:
#                 subsequences.append([first_element] + seq)
#
