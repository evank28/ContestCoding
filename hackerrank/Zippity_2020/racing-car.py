def minimumMovement(obstacleLanes: list) -> int:
    """
    >>> minimumMovement([2,1,2])
    1
    >>> minimumMovement([2,1,3,2])
    2
    """
    moves = 0
    current_lane = 2
    for i, obstacle in enumerate(obstacleLanes):
        if obstacle == current_lane:
            next_different_obstacle = \
                next_different(current_lane, obstacleLanes[i:])
            if next_different_obstacle == 0:
                current_lane = list({1, 2, 3} - {current_lane})[0]
            else:
                current_lane = \
                    list({1, 2, 3} - {current_lane, next_different_obstacle})[0]
            moves += 1
        else:
            continue
    return moves


def next_different(current_lane, obstacles) -> int:
    for obstacle in obstacles:
        if obstacle != current_lane:
            return obstacle
    return 0
