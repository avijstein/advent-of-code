import os

os.chdir('../github/advent/2020')

def navigate(nav):
    """
    given a set of navigation instructions, follow them one at a time
    Left/Right direction changes modify the Forward command
    East/South/West/North directions move in that direction
    """

    cards = ['E','S','W','N']
    current_heading = 0
    journey = {}

    for i in range(len(nav)):

        head, speed = nav[i][0], int(nav[i][1:])
        # print(head, speed)

        # if a direction, go in that direction
        if head not in ['L','R','F']:
            journey[head] = journey.get(head,0) + speed

        # if turning, change the current heading
        if head == 'L':
            current_heading = (current_heading - (speed // 90)) % 4
            # print('new heading:', cards[current_heading])

        if head == 'R':
            current_heading = (current_heading + (speed // 90)) % 4
            # print('new heading:', cards[current_heading])

        # if moving forward, go in the direction of current_heading
        if head == 'F':
            # print('moving to', cards[current_heading], 'at', speed)
            journey[cards[current_heading]] = journey.get(cards[current_heading], 0) + speed

    # print(journey)

    man = abs(journey['E'] - journey['W']) + abs(journey['N'] - journey['S'])
    return man


with open('./data/day12.txt') as f:
    nav = f.read().split('\n')[:-1]

    navigate(nav)




# fin
