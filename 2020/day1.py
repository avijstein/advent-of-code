import os

os.chdir('../github/advent')

nums = [1721,979,366,299,675,1456]

def advent1(nums):
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i], nums[j], nums[i]*nums[j]
    return 'no such expenses'


def advent1b(nums):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            for k in range(0,len(nums)):
                if (nums[i] + nums[j] + nums[k]) == 2020:
                    return nums[i], nums[j], nums[k], nums[i]*nums[j]*nums[k]
                print(nums[i], nums[j], nums[k])
        return 'no such expenses'



with open('2020/day1.txt') as f:
    new_lines = [int(x.replace('\n', '')) for x in f.readlines()]
    for i in range(0,10):
        print(i, new_lines[i])
    # print(advent1b(new_lines))

# print(advent1(nums))



# fin
