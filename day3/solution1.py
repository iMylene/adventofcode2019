import sys
data = sys.stdin.readlines()
wire_1 = data[0].split(',') 
wire_2 = data[1].split(',')

current_coord = (0,0)
wire_1_coords = set()
wire_2_coords = set()

for ipair in wire_1:
    if 'R' in ipair:
        for c in range(int(ipair[1:])):
            current_coord = (current_coord[0]+1,current_coord[1])
            wire_1_coords.add(current_coord)
    elif 'L' in ipair:
        for c in range(int(ipair[1:])):
            current_coord = (current_coord[0]-1,current_coord[1])
            wire_1_coords.add(current_coord)
    elif 'D' in ipair:
        for c in range(int(ipair[1:])):
            current_coord = (current_coord[0],current_coord[1]-1)
            wire_1_coords.add(current_coord)
    elif 'U' in ipair:
        for c in range(int(ipair[1:])):
            current_coord = (current_coord[0],current_coord[1]+1)
            wire_1_coords.add(current_coord)

current_coord = (0,0)
for ipair in wire_2:
    if 'R' in ipair:
        for c in range(int(ipair[1:])):
            current_coord = (current_coord[0]+1,current_coord[1])
            wire_2_coords.add(current_coord)
    elif 'L' in ipair:
        for c in range(int(ipair[1:])):
            current_coord = (current_coord[0]-1,current_coord[1])
            wire_2_coords.add(current_coord)
    elif 'D' in ipair:
        for c in range(int(ipair[1:])):
            current_coord = (current_coord[0],current_coord[1]-1)
            wire_2_coords.add(current_coord)
    elif 'U' in ipair:
        for c in range(int(ipair[1:])):
            current_coord = (current_coord[0],current_coord[1]+1)
            wire_2_coords.add(current_coord)

sts = []
for t in wire_1_coords.intersection(wire_2_coords):
    sts.append(sum([abs(x) for x in list(t)]))
print('We moeten invoeren: {}'.format(sorted(sts)[0]))