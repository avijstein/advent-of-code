import os

os.chdir('../github/advent/2020')

trees = 0

with open('data/day3.txt') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]
    print(lines)
    for i in range(len(lines)):
        line = lines[i][::-1]
        if len(line) >= i*3:
            print(i, line[i*3], line)
            if line[i*3] == '#':
                trees += 1
    print(trees)




# wrong guesses: 3

# fin
