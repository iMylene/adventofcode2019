import textwrap

data = input()
wide = 25
tall = 6
layerlength = wide*tall

splitted = textwrap.wrap(data, layerlength)

zeros = []
for layer in splitted:
    #find the layer that contains the fewest 0 digits
    zeros.append(layer.count('0'))
fewestzeros = min(zeros)

#what is the number of 1 digits multiplied by the number of 2 digits?
checklayer = splitted[(zeros.index(fewestzeros))]
ones = checklayer.count('1')
twos = checklayer.count('2')
print(ones*twos)