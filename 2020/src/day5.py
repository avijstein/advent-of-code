import os

os.chdir('../github/advent/2020')


def seating(ticket):
    """
    convert ticket string to binary, raise each to it's power, and add them up
    """
    power = [2**x for x in range(0,7)][::-1]

    binary_rows = [0 if x == 'F' else 1 for x in ticket[:7]]
    binary_cols = [0 if x == 'L' else 1 for x in ticket[-3:]]

    row = sum([binary_rows[i] * power[i] for i in range(len(binary_rows))])
    col = sum([binary_cols[i] * power[-3:][i] for i in range(len(binary_cols))])
    seat_id = (row * 8) + col

    return seat_id


with open('./data/day5.txt') as f:
    tickets = f.read().split('\n')
    highest_id = -1
    ids = []
    for ticket in tickets:
        id = seating(ticket)
        # print(highest_id, id)
        if id > highest_id:
            highest_id = id
        ids.append(id)
    # print(highest_id)


# not the best method, but quick and easy
# identify potentials and check each (there's only two and one's at the start)
sorted_ids = sorted(ids)
print(sorted_ids)
for i in range(1, len(sorted_ids)):
    if sorted_ids[i] - 1 not in sorted_ids:
        print(sorted_ids[i] - 1)


# fin
