a = 0
t = 0
c = 0
g = 0

text = input("give me a sequence of DNA :")
dna = list(text)
while len(dna) > 0:
    i = dna.pop()
    if i == "A":
        a = a + 1
    elif i == "T":
        t = t + 1
    elif i == "C":
        c = c + 1
    else:
        g = g + 1
        
dict = {'A' : a, 'T' : t, 'C' : c, 'G' : g}
print (dict)

from matplotlib import pyplot as plt 
labels = 'A', 'T', 'C', 'G'
sizes = [a, t, c, g]
explode = (0, 0, 0, 0)
plt.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)

plt.axis('equal')

plt.show()