import os

os.chdir('../github/advent/2020')



def upcoming_bus(start_time, bus_list):
    busses = [int(x) for x in bus_list.split(',') if x != 'x']
    next_bus, next_time = 100000, 100000
    for bus in busses:
        d, r = divmod(start,bus)
        upcoming = bus - r
        if upcoming < next_time:
            next_bus, next_time = bus, upcoming
    return next_bus * next_time


with open('./data/day13.txt') as f:
    schedule = f.read().split('\n')
    start, busses = int(schedule[0]), schedule[1]
    print(upcoming_bus(start, busses))



# fin
