def largestArea(samples):
    """
    Deceiving title -- returns the largest sidelength
    >>> largestArea([[1,1,1],[1,1,0],[1,0,1]])
    2
    >>> largestArea([[0,1,1],[1,1,0],[1,0,1]])
    1
    """
    dimension = len(samples)
    for side_length in range(dimension-1, 0, -1):
        for start_column in range(0, dimension - side_length):
            for start_row in range(0, dimension - side_length):
                if check_square(side_length, start_row, start_column, samples):
                    return side_length
    return 0

def check_square(dimension, top, left, samples):
    for row in samples[top:top+dimension]:
        if not all(row[left:left+dimension]):
            return False
    return True

