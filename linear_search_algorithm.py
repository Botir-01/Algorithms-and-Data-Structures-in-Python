# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
# and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number
# by turning over as few cards as possible. Write a function to help Bob locate the card.

# Create a variable position with the value 0.
# Check whether the number at index position in card equals query.
# If it does, position is the answer and can be returned from the function
# If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
# If the number was not found, return -1.

tests = []
case1 = {
    'input': {
        'card_list': [4, 5, 1, 3, 6, 4, 6],
        'target': 3
    },
    'output': 3
}

case2 = {
    'input': {
        'card_list': [4, 3, 6, 8, 534, 2, 1],
        'target': 2
    },
    'output': 5
}

case3 = {
    'input': {
        'card_list': [],
        'target': 7
    },
    'output': -1
}

tests.append(case1)
tests.append(case2)
tests.append(case3)


def find_position_by_linear(card_list, target):
    position = 0
    for i in range(len(card_list)):
        if card_list[position] == target:
            return position
        position += 1
    return -1


def run_test():
    test_number = 1
    for test in tests:
        result = find_position_by_linear(**test['input']) == test['output']
        if result:
            print(f"Test number {test_number} is succeded")
        else:
            print(f"Test number {test_number} is failed")
        test_number += 1

run_test()