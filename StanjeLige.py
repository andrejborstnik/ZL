from Liga import *
from os import path
import csv
stanjeLigeA={}
stanjeLigeB={}
stanjeLigeC={}
with open('zacetek.csv',encoding='utf-8') as f:
    k=0
    for line in f:
        if k!=0:
            a=line.split(';')
            ime=a[1]
            priimek=a[0]
            klub=a[2]
            kat=a[3]
            tocke=round(int(a[4][:-1]) + (int(a[4][:-1])-900)/4)
            if kat=='A':
                stanjeLigeA[(sumniki(ime),sumniki(priimek))]={'ime':ime,'priimek':priimek,'klub':klub,0:[0,tocke,False]}
            elif kat=='B':
                stanjeLigeB[(sumniki(ime),sumniki(priimek))]={'ime':ime,'priimek':priimek,'klub':klub,0:[0,tocke,False]}
            elif kat=='C':
                stanjeLigeC[(sumniki(ime),sumniki(priimek))]={'ime':ime,'priimek':priimek,'klub':klub,0:[0,tocke,False]}
##            elif kat == "Test":
##                stanjeLigeT[(sumniki(ime),sumniki(priimek))]={'ime':ime,'priimek':priimek,'klub':klub,0:[0,tocke,False]}
        k=1

#print(stanjeLigeA)
st_tekem=0
IP = 1

for st_lige in range(1,21):
    print(st_lige)
    if st_lige == 18:
        IP = 1.1
    if path.isfile('./Rezultati/OLP'+str(st_lige)+'.csv'):
        c,score = rezultati(st_lige,{'A':stanjeLigeA,'B':stanjeLigeB,'C':stanjeLigeC})
        for rezultati_kat in c['A'].values():
            stanjeLigeA=izracunLigeA(rezultati_kat,st_lige,stanjeLigeA, IP)
        stanjeLigeB=izracunLigeB(c['B'],st_lige,stanjeLigeB, IP)
        stanjeLigeC=izracunLigeC(c['C'],st_lige,stanjeLigeC, IP)
        st_tekem+=1
        #mankajociKlubi(stanjeLigeA)
        #mankajociKlubi(stanjeLigeB)
        #mankajociKlubi(stanjeLigeC)
        stanjeLige={'A':stanjeLigeA,'B':stanjeLigeB,'C':stanjeLigeC}
        vCsv(stanjeLige,st_tekem, score)

if path.isfile('./ResnaStanja/StanjeLige'+str(st_tekem)+'.csv'):
    g=open('OLP_2021.csv','w+',encoding='utf-8')
    with open('./ResnaStanja/StanjeLige'+str(st_tekem)+'.csv','r+',encoding='utf-8') as f:
        for i in f.readlines():
            g.write(i)
    g.close()
