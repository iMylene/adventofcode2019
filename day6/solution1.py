import sys

data = sys.stdin.readlines()
direct = len(data)
indirect = 0

dictOrb = {}
for orbit in data:
    l,r = orbit.strip('\n').split(')')
    dictOrb[r] = l

dynstore = {'COM': -1}
def find_indirect(val):
    global dynstore
    l = dictOrb[val]
    if l not in dynstore.keys():
        find_indirect(l)
    dynstore[val] = 1+dynstore[l]

for orbit in data:
    _,r = orbit.strip('\n').split(')')
    if r not in dynstore.keys():
        find_indirect(r)
    indirect += dynstore[r]
print(direct, indirect, indirect+direct)