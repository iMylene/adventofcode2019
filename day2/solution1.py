data = [ int(x) for x in input().split(',') ]
data[1] = 12
data[2] = 2

for i in range(0,len(data),4):
    if data[i] == 99:
        break

    x = data[i+1]
    y = data[i+2]
    z = data[i+3]

    a = data[x]
    b = data[y]
        
    if data[i] == 1:
        data[z] = a+b
    else:
        data[z] = a*b
print(data[0])