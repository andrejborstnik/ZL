def mankajociKlubi(stanjeLige):
    #Vstavi klube, tistim, ki jih nimajo.
    def sumniki(niz):
        sumniki=['š','č','ž','Š','Č','Ž','ć','Ć']
        nesumniki=['s','c','z','S','C','Z','c','C']
        a=''
        for i in niz:
            if i in sumniki:
                a+=nesumniki[sumniki.index(i)]
            else:
                a+=i
        return a
    f=open('klubi.txt',encoding='utf-8')
    for i in f.readlines():
        a=i.split(' ')
        if a and a!=['', '\n'] and a!=['\n']and len(a)==5:
            ime=str(a[0])
            priimek=str(a[1])
            klub=str(a[3])+' '+str(a[4])
            priimek=sumniki(priimek)
            ime=sumniki(ime)
            klub=klub[0:len(klub)-1]
            if (sumniki(ime),sumniki(priimek)) in stanjeLige.keys():
                if stanjeLige[(ime,priimek)].get('klub')==None or stanjeLige[(ime,priimek)].get('klub')=='':
                    stanjeLige[(ime,priimek)]['klub']=klub

        elif a and a!=['', '\n'] and a!=['\n']and len(a)==4:
            ime=str(a[0])
            priimek=str(a[1])
            klub=str(a[3])
            priimek=sumniki(priimek)
            ime=sumniki(ime)
            klub=klub[0:len(klub)-1]
            if (sumniki(ime),sumniki(priimek)) in stanjeLige.keys():
                if stanjeLige[(ime,priimek)].get('klub',None)==None or stanjeLige[(ime,priimek)].get('klub')=='':
                    stanjeLige[(ime,priimek)]['klub']=klub
    if ('Ana','Pribakovic Borstnik') in stanjeLige:
        stanjeLige['Ana','Pribakovic Borstnik']['klub']='OK Tivoli'
    if ('Radim','Hosek') in stanjeLige:
        stanjeLige['Radim','Hosek']['klub']='KOB Dobruska'
    f.close()
        
