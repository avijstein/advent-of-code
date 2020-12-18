import os

os.chdir('../github/advent/2020')

trees = 0

with open('data/day3.txt') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]
    print(lines)
    # print(len(lines), len(lines)//3)
    for i in range(len(lines)):
        # print(i,i*3)
        if len(lines[i]) >= i*3:
            if lines[i*3][i] == '#':
                trees += 1
            print(lines[i*3][i])
    print(trees)



# wrong guesses: 3

# fin
