#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    """
    >>> climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
    [6, 4, 2, 1]
    """
    unique_scores = list({score: None for score in scores}.keys())[::-1]
    ranks = []
    # last_score_index = 0
    for game_score in alice:
        for i, score in enumerate(unique_scores):
            if score > game_score:
                ranks.append(len(unique_scores) - i + 1)
                break
            elif score == game_score:
                ranks.append(len(unique_scores) - i)
                break
            elif i == len(unique_scores) - 1:
                ranks.append(1)
            else:
                continue

    return ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
