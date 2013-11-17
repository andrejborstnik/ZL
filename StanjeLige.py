from Liga import *
from os import path
import csv
stanjeLigeA={}
stanjeLigeB={}
stanjeLigeC={}
with open('zacetek.txt',encoding='utf-8') as f:
    for line in f:
        a=line.split(';')
        ime=a[0]
        priimek=a[1]
        klub=a[2]
        kat=a[3]
        tocke=a[4][:-1]
        if kat=='A':
            stanjeLigeA[(sumniki(ime),sumniki(priimek))]={'ime':ime,'priimek':priimek,'klub':klub,0:[0,int(tocke)]}
        elif kat=='B':
            stanjeLigeB[(sumniki(ime),sumniki(priimek))]={'ime':ime,'priimek':priimek,'klub':klub,0:[0,int(tocke)]}
        elif kat=='C':
            stanjeLigeC[(sumniki(ime),sumniki(priimek))]={'ime':ime,'priimek':priimek,'klub':klub,0:[0,int(tocke)]}

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
