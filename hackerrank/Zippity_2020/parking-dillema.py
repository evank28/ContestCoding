
def carParkingRoof(cars: list, k: int) -> int:
    """
    >>> carParkingRoof([ 2, 10, 8, 17 ], 3)
    9
    >>> carParkingRoof([ 1, 2, 3, 10 ], 4)
    10
    """
    cars = sorted(cars)
    min_dist = abs(cars[0]-cars[-1]) + 1
    for i in range(len(cars)-k):
        roof_dist = abs(cars[i] - cars[i+k-1]) + 1
        min_dist = min(min_dist, roof_dist)
    return min_dist


