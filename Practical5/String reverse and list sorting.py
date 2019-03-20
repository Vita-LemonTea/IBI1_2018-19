text = input("give me a string of word :")
answer = []
list (text)
text = text.split()

for i in text:
    list(i)
    i = i[::-1]
    ''.join(i)
    answer.append(i)
answer.sort()
answer.reverse()   
print (answer)
    


    
      