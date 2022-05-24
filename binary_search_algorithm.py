# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in increasing order,
# and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number
# by turning over as few cards as possible. Write a function to help Bob locate the card.

# Find the middle element of the list
# if it matches queried number, return the middle position as the answer.
# If it less than the queried number, then search the first half of the list
# If it is greater than the queried number, then search the second half of the list
# If no more elements remain, return -1

tests = []
case1 = {
    'input': {
        'card_list': [1, 2, 3, 4, 5, 6],
        'query': 1
    },
    'output': 0
}

case2 = {
    'input': {
        'card_list': [1, 2, 3, 4, 5, 6, 7],
        'query': 7
    },
    'output': 6
}

case3 = {
    'input': {
        'card_list': [],
        'query': 7
    },
    'output': -1
}

case4 = {
    'input': {
        'card_list': [3, 4, 5, 6, 7, 8, 9, 109],
        'query': 9
    },
    'output': 6
}

case5 = {
    'input': {
        'card_list': [3],
        'query': 3
    },
    'output': 0
}

case6 = {
    'input': {
        'card_list': [3, 4, 5, 6, 7, 8, 9, 109],
        'query': 65
    },
    'output': -1
}

case7 = {
    'input': {
        'card_list': [3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 109],
        'query': 7
    },
    'output': 4
}
tests.append(case1)
tests.append(case2)
tests.append(case3)
tests.append(case4)
tests.append(case5)
tests.append(case6)
tests.append(case7)


def test_location(card_list, mid, query):
    middle_number = card_list[mid]
    if middle_number == query:
        if mid - 1 >= 0 and card_list[mid-1] == query:
            return "left"
        else:
            return 'found'
    if middle_number > query:
        return "left"
    else:
        return "right"


def binary_search_algorithm(card_list, query):
    # Find the first, end and the middle positions of the list
    start = 0
    end = len(card_list) - 1
    while start <= end:
        middle = (start + end) // 2
        result = test_location(card_list, middle, query)
        if result == 'found':
            return middle

        elif result == 'left':
            end = middle - 1

        elif result == 'right':
            start = middle + 1
    return -1


for order, test in enumerate(tests):
    result = binary_search_algorithm(**test['input']) == test['output']
    if result:
        print('The test in order {} is passed'.format(order+1))
    else:
        print('The test in order {} is failed'.format(order+1))