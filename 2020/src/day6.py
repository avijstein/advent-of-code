import os

os.chdir('../github/advent/2020')


def shorten(form):
    return len(''.join(set(form)))


form, people = 'zrbvdpgykiqeakdvwzaiyregqpdxpkaievzrgyqakgcqvidpylzjsre', 4


def short_dictionary(form, people):
    dict, common_declarations = {}, 0
    for i in form:
        dict[i] = dict.get(i,0) + 1

    for key in dict:
        if dict[key] == people:
            common_declarations += 1

    return common_declarations


# this works when you can fold everyone into one group
with open('./data/day6.txt') as f:
    total_declarations = 0
    forms = f.read().split('\n\n')
    for line in forms:
        form, people = line.replace('\n',''), line.count('\n') + 1
        # print(form, people)
        # declaration = shorten(form)
        declaration = short_dictionary(form, people)
        total_declarations += declaration
    print(total_declarations)


# 3486 is too low for part 2



# fin
