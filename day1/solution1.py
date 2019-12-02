import sys, math
all_mass = [ int(x) for x in sys.stdin.readlines() ]
count = 0

for mass in all_mass:
    fuel = math.floor(mass/3) - 2
    count += fuel
print(count)