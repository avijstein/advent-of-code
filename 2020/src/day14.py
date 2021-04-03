import os

os.chdir('../github/advent/2020')


# data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0"""

# print(data)


def recode_num(num):
    bin_num = bin(int(num))[2:].zfill(36)
    new_num = []
    for i in range(len(mask)):
        if mask[i] != 'X':
            new_num.append(mask[i])
        else:
            new_num.append(bin_num[i])
    new_num = int(''.join(new_num),2)
    return new_num



mask = '0' * 36
mem = dict()

with open('./data/day14.txt') as f:
    lines = f.read().split('\n')[:-1]
    for line in lines:
        print(line)
        if "mask = " in line:
            mask = line.replace('mask = ', '')
        else:
            address, num = line[4:].split('] = ')
            mem[address] = recode_num(num)

print('total:', sum(mem.values()))




# for line in data.split('\n'):
#     if "mask = " in line:
#         mask = line.replace('mask = ', '')
#         # print('new mask:', mask)
#     else:
#         address, num = line[4:].split('] = ')
#         mem[address] = recode_num(num)

# print(mem.values())
# print('total:', sum(mem.values()))


# fin
