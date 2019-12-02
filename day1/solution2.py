import sys, math
all_mass = [ int(x) for x in sys.stdin.readlines() ]
count = 0

def calculateFuel(m):
    fuel = math.floor(m/3) - 2
    return fuel

for mass in all_mass:    
    fuel = calculateFuel(mass)
    if fuel >= 0:
        count += fuel
        moreFuel = fuel
    else:
        moreFuel = -1

    # need more fuel?
    while moreFuel >= 0:
        fuel = calculateFuel(fuel)
        if fuel >= 0:
            count += fuel
        moreFuel = math.floor(fuel/3) - 2

print(count)