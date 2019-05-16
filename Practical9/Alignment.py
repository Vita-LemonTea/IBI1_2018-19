seq1 = "MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
seq2 = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
seq3 = "WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"
s1n = "SOD2_human (NP_000627.2)"
s2n = "SOD2_mouse (NP_038699.2)"
s3n = "RandomSeq"

s1 = list(seq1) 
s2 = list(seq2)
s3 = list(seq3)

#input blosum62
text = open('blosum62.txt')
blosum62 = text.read()
lines = blosum62.strip().split('\n')

header = lines.pop(0)
columns = header.split()
matrix = {}
for row in lines:
    entries = row.split()
    row_name = entries.pop(0)
    matrix[row_name] = {}
    for column_name in columns:
      matrix[row_name][column_name] = entries.pop(0)

#Compare human sequence with mouse sequence
edit_distance = 0 
score = 0
for i in range(len(seq1)):
    x = matrix[s1[i]][s2[i]]
    x = int(x)
    score = score + x
    if s1[i] != s2[i]:  
        edit_distance += 1

identity = (len(seq1) - edit_distance) / len(seq1)
normalised = score / len(seq1)
print(s1n, seq1)
print(s2n, seq2)
print("BLOSUM score:", score)
print("Percentage identity:", identity)
print("normalised score:", normalised)


#Compare human sequence with random sequence
edit_distance = 0 
score = 0
for i in range(len(seq2)):
    x = matrix[s1[i]][s3[i]]
    x = int(x)
    score = score + x
    if s1[i] != s3[i]:  
        edit_distance += 1

identity = (len(seq2) - edit_distance) / len(seq2)
normalised = score / len(seq2)
print(' ')
print(s1n, seq1)
print(s3n, seq3)
print("BLOSUM score:", score)
print("Percentage identity:", identity)
print("normalised score:", normalised)

#Compare random sequence with mouse sequence
edit_distance = 0 
score = 0
for i in range(len(seq1)):
    x = matrix[s2[i]][s3[i]]
    x = int(x)
    score = score + x
    if s2[i] != s3[i]:  
        edit_distance += 1

identity = (len(seq1) - edit_distance) / len(seq1)
normalised = score / len(seq3)
print(' ')
print(s2n, seq2)
print(s3n, seq3)
print("BLOSUM score:", score)
print("Percentage identity:", identity)
print("normalised score:", normalised)

                    