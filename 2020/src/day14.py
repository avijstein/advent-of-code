import os

os.chdir('../github/advent/2020')


data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

# print(data)

def recode_num(mask, num):
    bin_num = bin(int(num))[2:].zfill(36)
    new_num = []
    for i in range(len(mask)):
        if mask[i] != 'X':
            new_num.append(mask[i])
        else:
            new_num.append(bin_num[i])
    new_num = int(''.join(new_num),2)
    return new_num


def address_mask(mask, address):
    xs = mask.count('X')
    adds = []
    for i in range(2**xs):
        fill = bin(i)[2:].zfill(xs)
        new_mask, counter = list(mask), 0
        for j in range(len(new_mask)):
            if new_mask[j] == 'X':
                new_mask[j] = fill[counter]
                counter += 1
        new_mask = ''.join(new_mask)
        new_add = recode_num(new_mask, address)
        adds.append(new_add)
    return adds



mask = "000000000000000000000000000000X1001X"
address = 42

print(address_mask(mask, address))




def v1(lines):
    mask = '0' * 36
    mem = dict()
    for line in lines:
        if "mask = " in line:
            mask = line.replace('mask = ', '')
        else:
            address, num = line[4:].split('] = ')
            mem[address] = recode_num(mask, num)
    total = sum(mem.values())
    return total

def v2(lines):
    mask = '0' * 36
    mem = dict()
    for line in lines:
        if "mask = " in line:
            mask = line.replace('mask = ', '')
        else:
            address, num = line[4:].split('] = ')
            mem[address] = recode_num(mask, num)
    total = sum(mem.values())
    return total


with open('./data/day14.txt') as f:
    lines = f.read().split('\n')[:-1]
    # print(v2(lines))




# fin
