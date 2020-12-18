import os, re

os.chdir('../github/advent/2020')

rules = ['1-3 a', '1-3 b', '2-9 c']
passwords = ['abcde', 'cdefg', 'ccccccccc']


def letter_count(rules, passwords):
    """
    input: list of strings (rules) and list of strings (passwords)
    parses rules to count for that number of a letter in the passwords
    returns int of how many are valid
    """
    valid = 0
    for i in range(len(rules)):
        match = re.search('(^[0-9]+)-([0-9]+) (\w)', rules[i])
        counts = passwords[i].count(match.group(3))
        if counts >= int(match.group(1)) and counts <= int(match.group(2)):
            valid += 1
    return valid


# print(letter_count(rules, passwords))

def letter_index(rules, passwords):
    """
    input: list of strings (rules) and list of strings (passwords)
    parses rules to find values of the password at those indices
    returns int of how many are valid (have exactly one of the letter)
    """
    valid = 0
    for i in range(len(rules)):
        match = re.search('(^[0-9]+)-([0-9]+) (\w)', rules[i])
        first_index, second_index = int(match.group(1)) - 1, int(match.group(2)) - 1
        word_check = passwords[i][first_index] + passwords[i][second_index]
        if word_check.count(match.group(3)) == 1:
            valid += 1
    return valid

# print(letter_index(rules, passwords))


with open('data/day2.txt') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]
    rules,passwords = [],[]
    for line in lines:
        a,b = line.split(': ')
        rules.append(a)
        passwords.append(b)

    print(letter_count(rules, passwords))
    print(letter_index(rules, passwords))





# fin
