import textwrap

data = input()
wide = 25
tall = 6
layerlength = wide*tall
splitted = textwrap.wrap(data, layerlength)

#The layers are rendered with the first layer in front and the last layer in back.
def findcolor(i):
    for index in range(len(splitted)):
        layer = splitted[index]
        pixel = int(layer[i])
                
        if pixel != 2:
            if pixel==0:
                return ' '
            if pixel==1:
                return '#'
            return str(pixel)

#full image can be found by determining the top visible pixel in each position
listmessage = []
for i in range(tall):
    for j in range(wide):
        pixel = i*wide + j
        listmessage.append(findcolor(pixel))
    listmessage.append('\n')
message = ''.join(listmessage)
print(message)