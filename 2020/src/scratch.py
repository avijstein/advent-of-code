# Advent Challenges

## Day 1

nums = [1721,979,366,299,675,1456]

def advent1(nums):
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i], nums[j], nums[i]*nums[j]
    return 'no such expenses'

# advent1(nums)


## Day 2
import re

rules = ['1-3 a', '1-3 b', '2-9 c']
passwords = ['abcde', 'cdefg', 'ccccccccc']


def advent2(rules, passwords):
    new_rules = []
    for i in rules:
        match = re.search('(^[0-9]+)-([0-9]+) (\w)', i)
        pattern = match.group(3) + '{' + match.group(1) + ',' + match.group(2) + '}'
        new_rules.append(pattern)

    dict = {new_rules[i]: passwords[i] for i in range(len(new_rules))}

    valid = 0
    for keys in dict:
        if re.search(keys, dict[keys]):
            valid += 1
    return valid

# advent2(rules, passwords)


## Day 3

def advent3():
    trees = 0; i = 0
    with open('./advent/day3_trees.txt') as f:
        for line in f:
            if line[i*3] == '#':
                trees += 1
            i += 1
        return trees


# advent3()


## Day 4


def advent4():
    valid = 0
    with open('./advent/day4_passports.txt') as f:
        passports = f.read().split('\n\n')
        for line in passports:
            passport = line.replace('\n','')
            if passport.count(':') == 8:
                valid += 1
            elif passport.count(':') == 7 and passport.find('cid:') == -1:
                valid += 1
        return valid

# advent4()


## Day 5

# this seems too easy...there are 128 rows (max row number is 127) and 8 columns (max column number is 7)
# so 127 * 8 + 7 = 1023




# fin
