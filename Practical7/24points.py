from fractions import Fraction
numbers = input("Please input numbers to computer 24(use ',' to divide them):")
numbers = numbers.split(",")
nu = []
for i in numbers:
    i = int(i)
    nu.append(i)

#check the input numbers     
for n in nu:
    if n >= 24 or n < 1:
        print("The input number must be integers from 1 to 23")
        break

num = list(map(int,nu))
#recursion times
count = 0 

#n is len(num) 
def dfs(n):
    global count
    count = count +1
    
    if n == 1:
        if(float(num[0])==24):
            return 1
        else:
            return 0
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):
            a = num[i]
            b = num[j]
            num[j] = num[n-1]
            
            num[i] = a+b
            if(dfs(n-1)):
                return 1
            
            num[i] = a-b
            if(dfs(n-1)):
                return 1  
            
            num[i] = b-a
            if(dfs(n-1)): 
                return 1 
            
            num[i] = a*b
            if(dfs(n-1)): 
                return 1  
            
            if a:
                #floats are not precise
                num[i] = Fraction(b,a)
                if(dfs(n-1)): 
                    return 1 
                
            if b:
                num[i] = Fraction(a,b)
                if(dfs(n-1)): 
                    return 1 
            #Backtracking  
            num[i] = a
            num[j] = b
    return 0 

#output the results
if (dfs(len(num))): 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)
