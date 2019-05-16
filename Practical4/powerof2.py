x = 2019    #Give a number no larger than 2^13
n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]    #powers of 2
power = []

answer = str(x)+" is "

#Write x as a sum of powers of 2
while len(n)>0:        
    j = n.pop()
    if x >= 2**j:
        x = x - 2**j
        answer = answer + "2**" + str(j) + "+"
        power.append(j)

#To remove the last "+" from the answer
answer = list(answer)           
answer.pop()
answer = ''.join(answer)


print(answer)    #output the answer
        
    
    
