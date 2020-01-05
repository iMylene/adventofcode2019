# The value is within the range given in your puzzle input.
begin = int(172851)
end = int(675869)
numlist = [str(x) for x in list(range(begin,end))]

count = 0
for x in numlist:
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).'''   

    if sorted(x) == list(x) and len(set(x)) < 6:
        count += 1

print(count)