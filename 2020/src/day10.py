import os

os.chdir('../github/advent/2020')


def one_arrangement(jolts):
    """
    for each (sorted) int in the list, count the jump from the previous one
    multiple the number of jumps by one and by three
    """

    single, triple = 1, 1

    for i in range(1,len(jolts)):
        print(jolts[i-1], jolts[i])
        if jolts[i] - jolts[i-1] == 1:
            single += 1
        if jolts[i] - jolts[i-1] == 3:
            triple += 1

    return single * triple


with open('./data/day10.txt') as f:
    jolts = f.read().split('\n')[:-1]
    jolts = sorted([int(x) for x in jolts])

    # print(jolts)

    one_arrangement(jolts)




# fin
