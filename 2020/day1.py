import os

os.chdir('../github/advent')

nums = [1721,979,366,299,675,1456]


def advent1a(nums):
    """
    given a list of ints, loop through the list to find every pair
    Add them together, and see if any equal 2020.
    """
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i], nums[j], nums[i]*nums[j]
    return 'no such expenses'


def advent1b(nums):
    """
    given a list of ints, do the same as advent1a, but for three numbers.
    """
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            for k in range(j,len(nums)):
                if (nums[i] + nums[j] + nums[k]) == 2020:
                    return nums[i], nums[j], nums[k], nums[i]*nums[j]*nums[k]
    return 'no such expenses'



with open('2020/day1.txt') as f:
    new_lines = [int(x.replace('\n', '')) for x in f.readlines()]
    print(advent1a(new_lines))
    print(advent1b(new_lines))




# fin
