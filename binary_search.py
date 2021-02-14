# =================================Binary=Search============================
# the time complexity of binary search is O(log N) and its space complexity is O(1).

# Find the middle element of the list.
# If it matches queried number, return the middle position as the answer.
# If it is less than the queried number, then search the first half of the list
# If it is greater than the queried number, then search the second half of the list
# If no more elements remain, return -1.

def test_location(items, target, mid):
    if items[mid] == target:
        if mid-1 >= 0 and items[mid-1] == target:
            return 'left'
        else:
            return 'found'
    elif items[mid] < target:
        return 'left'
    else:
        return 'right'


def binary_search(items, target):
    left_side, right_side = 0, len(items) - 1
    while left_side <= right_side:
        mid = (left_side + right_side) // 2
        result = test_location(items, target, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            right_side = mid - 1
        elif result == 'right':
            left_side = mid + 1
    return -1

# Furthermore, as the size of the input grows larger, the difference only gets bigger. For a list 10 times, the size,
# linear search would run for 10 times longer, whereas binary search would only require 3 additional operations! (can
# you verify this?) That's the real difference between the complexities O(N) and O(log N). Another way to look at it
# is that binary search runs c * N / log N times faster than linear search, for some fixed constant c. Since log N
# grows very slowly compared to N, the difference gets larger with the size of the input.


def generic_binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
