'''find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700'''
mult = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        mult.append(str(x))
    
print(', '.join(mult))
