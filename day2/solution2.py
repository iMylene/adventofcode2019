data_orig = [ int(x) for x in input().split(',') ]
for pi in range(100):
    for pj in range(100):
        data = data_orig[:]
        data[1] = pi
        data[2] = pj

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

        if data[0] == 19690720:
            print(100*pi+pj)