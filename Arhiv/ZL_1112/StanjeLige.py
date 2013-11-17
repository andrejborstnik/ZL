from Liga import *
from os import path
from bla import mankajociKlubi
import csv
stanjeLigeA={}
stanjeLigeB={}
stanjeLigeC={}
with open('zacetek.txt',encoding='utf-8') as f:
    for line in f:
        a=str(line).split()
        b=True
        ime=''
        priimek=''
        for i in a[0]:
            if i==' ':
                pass
            else:
                if ime=='Žan':
                    ime+=' '
                ime+=i
        for i in a[1:]:
            for j in i:
                if j!=' ' and not j.isnumeric():
                    priimek+=j
            if b and len(a[1:])>2:
                priimek+=' '
                b=not b
        stanjeLigeA[(sumniki(ime),sumniki(priimek))]={'ime':ime,'priimek':priimek,0:[0,int(a[len(a)-1])]}
st_tekem=0
for st_lige in range(1,20):
    if path.isfile('./Rezultati/ZL'+str(st_lige)+'.csv'):
        c=rezultati(st_lige,{'A':stanjeLigeA,'B':stanjeLigeB,'C':stanjeLigeC})
        stanjeLigeA=izracunLigeA(c['A'],st_lige,stanjeLigeA)
        stanjeLigeB=izracunLigeB(c['B'],st_lige,stanjeLigeB)
        stanjeLigeC=izracunLigeC(c['C'],st_lige,stanjeLigeC)
        st_tekem+=1
        mankajociKlubi(stanjeLigeA)
        mankajociKlubi(stanjeLigeB)
        mankajociKlubi(stanjeLigeC)
        stanjeLige={'A':stanjeLigeA,'B':stanjeLigeB,'C':stanjeLigeC}
        vCsv(stanjeLige,st_tekem)
if path.isfile('./ResnaStanja/StanjeLige'+str(st_tekem)+'.csv'):
    g=open('ZL_2011_2012.csv','w+',encoding='utf-8')
    with open('./ResnaStanja/StanjeLige'+str(st_tekem)+'.csv','r+',encoding='utf-8') as f:
        for i in f.readlines():
            g.write(i)
    g.close()
