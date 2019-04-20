# created by panhongbing
# This code displays the Collatz sequence of n and ends when reaches 1 for the first time
n = 17  #give an integer n
while n != 1:    
     if n % 2 == 0:   #If n is even, n is divided by 2 
        n = n / 2
     else:         #If n is odd, n is multiplying by 3 and adding 1
        n = 3 * n + 1
     print(n)    #out put n