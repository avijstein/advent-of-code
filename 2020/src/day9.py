import os

os.chdir('../github/advent/2020')


def doesnt_add_up(digits):
    """
    for each item, look at the previous 25 items.
    if the current item subtracted from any of those previous items is in the set, it's a match.
    """
    for i in range(25, len(digits)):
        item = digits[i]
        # print(i, item)
        possibilities = digits[i-25:i]
        # print(possibilities)
        matches = 0
        for j in possibilities:
            test_item = item - j
            if test_item in possibilities:
                # print('match:', item, test_item, j)
                matches += 1
        if matches == 0:
            return item
            # print('no matches for item:', item)


def digit_collection(digits):
    """
    for each item, start adding up each subsequent item unless they get too big, then move on.
    if there's a series of items that adds up exactly to the target, then return that.
    """
    for i in range(0,len(digits)):
        j, total = i + 1, 0
        while total < 1504371145 and j < len(digits):
            # print(i,j, digits[i:j], sum(digits[i:j]))
            collection = digits[i:j]
            total = sum(digits[i:j])
            j += 1
        if total == 1504371145 and len(collection) > 1:
            # print('found it!', i, j, total, collection)
            # print('secret:', min(collection) + max(collection))
            return min(collection) + max(collection)


with open('./data/day9.txt') as f:
    digits = f.read().split('\n')[:-1]
    digits = [int(x) for x in digits]

    # part one
    doesnt_add_up(digits)

    # part two
    digit_collection(digits)




# fin
