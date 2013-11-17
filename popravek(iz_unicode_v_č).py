f=open('./Rezultati/ZL3a.csv','r+',encoding='utf-8')
g=open('./Rezultati/ZL3.csv','w+',encoding='utf-8')
for i in f:
    for j in i:
        if j=='è':
            g.write('č')
        elif j=='æ':
            g.write('ć')
        elif j=='È':
            g.write('Č')
        else:
            g.write(j)
g.close()
f.close()
