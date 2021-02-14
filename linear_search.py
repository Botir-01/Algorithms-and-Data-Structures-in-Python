# ==================================Linear=Search===============================
# the time complexity of linear search is O(N) and its space complexity is O(1).

# Create a variable position with the value 0.
# Check whether the number at index position in card equals query.
# If it does, position is the answer and can be returned from the function
# If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
# If the number was not found, return -1.

def linear_search(items, target):
    """
    :param items: list of characters
    :param target: an item to be found in items
    :return: target if it is in the list, otherwise return -1
    """
    position = 0
    while position < len(items):
        if items[position] == target:
            return position
        position += 1
    return -1
