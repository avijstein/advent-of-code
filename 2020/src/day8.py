import os

os.chdir('../github/advent/2020')


with open('./data/day8.txt') as f:
    example = f.read().split('\n')[:-1]

    print(example)

    i, ixs, inc = 0, [], 0

    # every time we visit an instruction, keep track
    while i not in ixs:
        if i > len(example) - 1:
            break

        ixs.append(i)

        # identify the command type and value
        cmd_type = example[i][:3]
        if example[i][4:5] == '+':
            cmd_value = int(example[i][5:])
        else:
            cmd_value = int(example[i][5:]) * -1

        print(i, example[i])

        # specific instructions for each command type
        # diagnostics are commented out
        if cmd_type == 'nop':
            # print('nothing happened')
            pass
        elif cmd_type == 'acc':
            inc = inc + cmd_value
            # print('inc is now', inc)
        elif cmd_type == 'jmp':
            i = i + cmd_value - 1
            # print('jumping!')
            pass

        i += 1

    print('')
    print('indexes visited', len(ixs))
    print('final acc value:', inc)


# fin
