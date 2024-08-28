In = eval(input())
saída = []

for i in range(len(In[0])):
    if len(saída) < In[1]:
        saída.append(In[0][i])
        i += 1
    else:
        savenum = saída[0]
        sub = False
        for j in range(len(saída)):
            if saída[j] > In[0][i] and sub == False:
                savenum = saída[j]
                saída[j] = In[0][i]
                sub = True
                j += 1
            else:
                if savenum < saída[j]:
                    saída[j] = savenum
                    j += 1

print(saída)