def izracunLigeA(rezultatiTekme,st_tekme,stanjeLigeA,IP=1):
    #'st_tekme' je št ZL(npr. pri ZL2, je to 2).
    #IP je vrednost tekme(1.2 pomeni, da je tekmo vredna 20 % več).
    
    def povprecje(seznam):
        #Vrne povprecje točk/časov v seznamu.
        if seznam:
            vsota=0
            for x in seznam:
                vsota+=x
            povprecje=vsota/len(seznam)
            return povprecje
    
    def standardnaDeviacija(seznam):
        #Iz seznama točk/časov tekmovalccev izračuna standardno deviacijo.
        if seznam:
            Povprecje=povprecje(seznam)
            vsota=0
            for x in seznam:
                vsota+=(Povprecje-x)**2
            standardnaDeviacija=(vsota/len(seznam))**0.5
            return standardnaDeviacija
    
    #Sestavljamo seznam z časi in točkami.
    seznamCasov=[]
    seznamTock=[]
    for (x,y) in rezultatiTekme.keys():
        if (x,y) not in stanjeLigeA.keys():
            stanjeLigeA[(x,y)]={0:[0,500]}
        if stanjeLigeA[(x,y)][0][1]>600:
            seznamTock.append(stanjeLigeA[(x,y)][0][1])
            if rezultatiTekme[(x,y)]!='mp':
                seznamCasov.append((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2])

    #Računamo točke(glej formulo na iof strani) in zapisujemo rezultat/tocke/mesto.
    ST=standardnaDeviacija(seznamCasov)
    SP=standardnaDeviacija(seznamTock)
    MT=povprecje(seznamCasov)
    MP=povprecje(seznamTock)
    seznamCasov=[]
    for (x,y) in rezultatiTekme.keys():
        if rezultatiTekme[(x,y)]!='mp':
            seznamCasov.append((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2])
    seznamCasov.sort()
    for x,y in rezultatiTekme.keys():
        if rezultatiTekme[(x,y)]!='mp':
            RT=(rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]
            for i in range(len(seznamCasov)):
                if seznamCasov[i]==RT:
                    mesto=i+1
                    break
            RP=(MP+SP*(MT-RT)/ST)*IP
            stanjeLigeA[(x,y)][st_tekme]=[rezultatiTekme[(x,y)],round(RP),mesto]
        else:
            stanjeLigeA[(x,y)][st_tekme]=['mp','niTock']
        vsota_=0
        k=0
        for i,j in stanjeLigeA[(x,y)].items():
            if i not in ['sestevek','povprecje'] and j[1]!='niTock' and j[1]>0:
                vsota_+=round(j[1])
                k+=1
            else:
                pass
        if k!=0:
            stanjeLigeA[(x,y)][0]=[0,round(vsota_/k)]

    #Računamo skupni seštevek lige.
    for x,y in stanjeLigeA:
        seznam=[]
        for i,j in stanjeLigeA[(x,y)].items():
            if i in [k for k in range(1,20)] and j[1]!='niTock' and j[1]>0:
                seznam.append(j[1])
        seznam.sort()
        seznam=seznam[::-1]
        if len(seznam)==0:
            pass
        elif len(seznam)>=4:
            stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:3])
            stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:3])/4)
        else:
            stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:len(seznam)])
            stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:len(seznam)])/len(seznam))
    return stanjeLigeA



def izracunLigeB(rezultatiTekme,st_tekme,stanjeLigeB={},IP=1):
    #Sestavljamo seznam z časi.
    seznamCasov=[]
    for (x,y) in rezultatiTekme.keys():
        if (x,y) not in stanjeLigeB.keys():
            stanjeLigeB[(x,y)]={}
        if rezultatiTekme[(x,y)]!='mp':
            seznamCasov.append((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2])
    casNajboljsega=min(seznamCasov)
    seznamCasov.sort()
    seznamCasov=seznamCasov[::-1]
    for (x,y) in rezultatiTekme.keys():
        if rezultatiTekme[(x,y)]!='mp':
            for i in range(len(seznamCasov)):
                if seznamCasov[i]==(rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]:
                    mesto=len(seznamCasov)-i
                    break
        
            stanjeLigeB[(x,y)][st_tekme]=[rezultatiTekme[(x,y)],round((len(seznamCasov)-mesto+1+100*casNajboljsega/((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]))*IP),mesto]
        else:
            stanjeLigeB[(x,y)][st_tekme]=['mp','niTock']
            
    #Računamo skupni seštevek lige.
    stanjeLigeA=stanjeLigeB
    for x,y in stanjeLigeA:
        seznam=[]
        for i,j in stanjeLigeA[(x,y)].items():
            if i in [k for k in range(1,20)] and j[1]!='niTock':
                seznam.append(j[1])
        seznam.sort()
        seznam=seznam[::-1]
        if len(seznam)==0:
            pass
        elif len(seznam)>=4:
            stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:3])
            stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:3])/4)
        else:
            stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:len(seznam)])
            stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:len(seznam)])/len(seznam))

    return stanjeLigeA



def izracunLigeC(rezultatiTekme,st_tekme,stanjeLigeC={},IP=1):
    stanjeLigeB=stanjeLigeC
    #Sestavljamo seznam z časi.
    seznamCasov=[]
    for (x,y) in rezultatiTekme.keys():
        if (x,y) not in stanjeLigeB.keys():
            stanjeLigeB[(x,y)]={}
        if rezultatiTekme[(x,y)]!='mp':
            seznamCasov.append((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2])
    casNajboljsega=min(seznamCasov)
    seznamCasov.sort()
    seznamCasov=seznamCasov[::-1]
    for (x,y) in rezultatiTekme.keys():
        if rezultatiTekme[(x,y)]!='mp':
            for i in range(len(seznamCasov)):
                if seznamCasov[i]==(rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]:
                    mesto=len(seznamCasov)-i
                    break
            stanjeLigeB[(x,y)][st_tekme]=[rezultatiTekme[(x,y)],round((len(seznamCasov)-mesto+1+100*casNajboljsega/((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]))*IP),mesto]
        else:
            stanjeLigeB[(x,y)][st_tekme]=['mp','niTock']
            
    #Računamo skupni seštevek lige.
    stanjeLigeA=stanjeLigeB
    for x,y in stanjeLigeA:
        seznam=[]
        for i,j in stanjeLigeA[(x,y)].items():
            if i in [k for k in range(1,20)] and j[1]!='niTock':
                seznam.append(j[1])
        seznam.sort()
        seznam=seznam[::-1]
        if len(seznam)==0:
            pass
        elif len(seznam)>=4:
            stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:3])
            stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:3])/4)
        else:
            stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:len(seznam)])
            stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:len(seznam)])/len(seznam))

    return stanjeLigeA



def rezultati(st_lige):
    #Vrne rezultate tekme v slovarju oblike {'A':rezultatiTekmeA,...}.
    rezultatiTekmeA={}
    rezultatiTekmeB={}
    rezultatiTekmeC={}
    import csv
    with open('./Rezultati/ZL'+str(st_lige)+'.csv',encoding='utf-8') as f:
        reader=csv.reader(f)
        rownum=0
        for row in reader:
            if rownum==1:
                header=str(row[0]).split(';')
            elif rownum==0:
                pass
            else:
                colnum=0
                for col in str(row[0]).split(';'):
                    if colnum>=len(header):
                        break
                    if header[colnum]=='First name':
                        ime=col
                    elif header[colnum]=='Surname':
                        priimek=col
                    elif header[colnum]=='Short':
                        kategorija=col
                    elif header[colnum]=='Time':
                        if col!='':
                            cas1=col
                        else:
                            cas1=False
                    else:
                        pass            
                    colnum+=1
                if not cas1:
                    cas='mp'
                else:
                    cas=['','','']
                    st_dvopicij=0
                    for y in cas1:
                        if y!=':'and y!='"':
                            cas[st_dvopicij]+=str(y)
                        elif y=='"':
                            pass
                        else:
                            st_dvopicij+=1
                    if cas[2]=='':
                        cas[2]=cas[1]
                        cas[1]=cas[0]
                        cas[0]=str(0)
                    cas=[int(cas[0]),int(cas[1]),int(cas[2])]
                a=''
                for i in ime:
                    if i!='"':
                        a+=i
                ime=a
                a=''
                for i in priimek:
                    if i!='"':
                        a+=i
                priimek=a
                a=''
                for i in kategorija:
                    if i!='"':
                        a+=i
                kategorija=a
                sumniki=['š','č','ž','Š','Č','Ž','ć','Ć']
                nesumniki=['s','c','z','S','C','Z','c','C']
                ime1=''
                priimek1=''
                for i in ime:
                    if i in sumniki:
                        ime1+=nesumniki[sumniki.index(i)]
                    else:
                        ime1+=i
                for i in priimek:
                    if i==' ':pass
                    elif i in sumniki:
                        priimek1+=nesumniki[sumniki.index(i)]
                    else:
                        priimek1+=i
                if kategorija== "A":
                    rezultatiTekmeA[(ime1,priimek1)]=cas
                elif kategorija== "B":
                    rezultatiTekmeB[(ime1,priimek1)]=cas
                elif kategorija== "C":
                    rezultatiTekmeC[(ime1,priimek1)]=cas
                else:
                    pass
            rownum+=1
    rezultatiTekme={'A':rezultatiTekmeA,'B':rezultatiTekmeB,'C':rezultatiTekmeC}
    return rezultatiTekme
def vCsv(stanjeLige,st_tekem):
    with open('./Stanja_racunana/StanjeLige'+str(st_tekem)+'.csv','w+',encoding='utf-8') as f:
        f.write('Surname;First name;Class;Time;Pl;Points;Sum;Average\n')
        mestaA=[]
        mestaB=[]
        mestaC=[]
        for k in ['A','B','C']:
            for x,y in stanjeLige[k]:
                if stanjeLige[k][x,y].get('sestevek',None)!=None:
                    if k=='A':
                        mestaA.append(stanjeLige[k][x,y]['sestevek'])
                    elif k=='B':
                        mestaB.append(stanjeLige[k][x,y]['sestevek'])
                    elif k=='C':
                        mestaC.append(stanjeLige[k][x,y]['sestevek'])
                else:pass
        mestaA.sort()
        mestaB.sort()
        mestaC.sort()
        mestaA=mestaA[::-1]
        mestaB=mestaB[::-1]
        mestaC=mestaC[::-1]
        for k in ['A','B','C']:
            uporabljeni=[]
            i=0
            if k=='A':
                while i<len(mestaA):
                    for (x,y) in stanjeLige[k]:
                        if stanjeLige[k][x,y].get('sestevek',None)==None:
                                pass
                        else:
                            if (x,y) not in uporabljeni and mestaA[i]==stanjeLige[k][x,y]['sestevek']:
                                if stanjeLige[k][x,y].get(st_tekem,None)==None:
                                    f.write(y+';'+x+';'+k+';'+''+';'+''+';'+'')
                                elif stanjeLige[k][x,y][st_tekem][0]!='mp':
                                    cas=''
                                    podpicja=0
                                    for j in range(3):
                                        for i in str(stanjeLige[k][x,y][st_tekem][0][j]):
                                            cas+=i
                                        podpicja+=1
                                        if podpicja!=3:
                                            cas+=':'
                                    f.write(y+';'+x+';'+k+';'+cas+';'+str(stanjeLige[k][x,y][st_tekem][2])+';'+str(stanjeLige[k][x,y][st_tekem][1]))
                                else:
                                    f.write(y+';'+x+';'+k+';'+'mp'+';'+''+';'+'')
                                if stanjeLige[k][x,y].get('sestevek',None)!=None:
                                    for i in range(1,st_tekem +1):
                                        if stanjeLige[k][x,y].get(i,None)!=None:
                                            f.write(';'+str(stanjeLige[k][x,y][i][1]))
                                        else:
                                            f.write(';'+'')
                                    f.write(';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')
                                i+=1
                                uporabljeni.append((x,y))

            elif k=='B':
                while i<len(mestaB):
                    for (x,y) in stanjeLige[k]:
                        if stanjeLige[k][x,y].get('sestevek',None)==None:
                                pass
                        else:
                            if (x,y) not in uporabljeni and mestaA[i]==stanjeLige[k][x,y]['sestevek']:    
                                if stanjeLige[k][x,y].get(st_tekem,None)==None:
                                    f.write(y+';'+x+';'+k+';'+''+';'+''+';'+'')
                                elif stanjeLige[k][x,y][st_tekem][0]!='mp':
                                    cas=''
                                    podpicja=0
                                    for j in range(3):
                                        for i in str(stanjeLige[k][x,y][st_tekem][0][j]):
                                            cas+=i
                                        podpicja+=1
                                        if podpicja!=3:
                                            cas+=':'
                                    f.write(y+';'+x+';'+k+';'+cas+';'+str(stanjeLige[k][x,y][st_tekem][2])+';'+str(stanjeLige[k][x,y][st_tekem][1]))
                                else:
                                    f.write(y+';'+x+';'+k+';'+'mp'+';'+''+';'+'')
                                if stanjeLige[k][x,y].get('sestevek',None)!=None:
                                    for i in range(1,st_tekem +1):
                                        if stanjeLige[k][x,y].get(i,None)!=None:
                                            f.write(';'+str(stanjeLige[k][x,y][i][1]))
                                        else:
                                            f.write(';'+'')
                                    f.write(';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')
                                i+=1
                                uporabljeni.append((x,y))

            elif k=='C':
                while i<len(mestaC):
                    for (x,y) in stanjeLige[k]:
                        if stanjeLige[k][x,y].get('sestevek',None)==None:
                                pass
                        else:
                            if (x,y) not in uporabljeni and mestaA[i]==stanjeLige[k][x,y]['sestevek']:    
                                if stanjeLige[k][x,y].get(st_tekem,None)==None:
                                    f.write(y+';'+x+';'+k+';'+''+';'+''+';'+'')
                                elif stanjeLige[k][x,y][st_tekem][0]!='mp':
                                    cas=''
                                    podpicja=0
                                    for j in range(3):
                                        for i in str(stanjeLige[k][x,y][st_tekem][0][j]):
                                            cas+=i
                                        podpicja+=1
                                        if podpicja!=3:
                                            cas+=':'
                                    f.write(y+';'+x+';'+k+';'+cas+';'+str(stanjeLige[k][x,y][st_tekem][2])+';'+str(stanjeLige[k][x,y][st_tekem][1]))
                                else:
                                    f.write(y+';'+x+';'+k+';'+'mp'+';'+''+';'+'')
                                if stanjeLige[k][x,y].get('sestevek',None)!=None:
                                    for i in range(1,st_tekem +1):
                                        if stanjeLige[k][x,y].get(i,None)!=None:
                                            f.write(';'+str(stanjeLige[k][x,y][i][1]))
                                        else:
                                            f.write(';'+'')
                                    f.write(';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')
                                i+=1
                                uporabljeni.append((x,y))
                if stanjeLige[k][x,y].get('sestevek',None)==None:
                    pass
                elif stanjeLige[k][x,y].get(st_tekem,None)==None:
                    f.write(y+';'+x+';'+k+';'+''+';'+''+';'+''+';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')
                elif stanjeLige[k][x,y][st_tekem][0]!='mp':
                    cas=''
                    podpicja=0
                    for j in range(3):
                        for i in str(stanjeLige[k][x,y][st_tekem][0][j]):
                            cas+=i
                        podpicja+=1
                        if podpicja!=3:
                            cas+=':'
                    f.write(y+';'+x+';'+k+';'+cas+';'+str(stanjeLige[k][x,y][st_tekem][2])+';'+str(stanjeLige[k][x,y][st_tekem][1])+';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')
                else:
                    f.write(y+';'+x+';'+k+';'+'mp'+';'+''+';'+''+';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')


