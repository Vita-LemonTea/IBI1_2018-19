x = 3832
i = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
good = []
bad = []
answer = str(x)+" is "
while len(i)>0:
    j = i.pop()
    if x >= 2**j:
        x = x - 2**j
        good.append(j)
    else:
        bad.append(j)
while len(good)>1:
    a = good.pop()
    answer = answer + "2**" + str(a) + "+"
b = good.pop()
print(answer,"2**",b)
        
    
    
