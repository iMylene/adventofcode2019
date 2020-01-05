import sys

data = sys.stdin.readlines()
direct = len(data)
indirect = 0

dictOrb = {}
for orbit in data:
    l,r = orbit.strip('\n').split(')')
    dictOrb[r] = l

def tocom(val):
    l = dictOrb[val]
    yourroute = set()
    while l != 'COM':
        yourroute.add(l)
        l = dictOrb[l]
    return yourroute

you = tocom('YOU')
san = tocom('SAN')
print('Less Naive: {}'.format(len(san)+len(you)-2*len(san.intersection(you))))