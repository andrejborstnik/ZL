def sumniki(niz):
    #Vrne enak niz, brez sumnikov.
    sumniki=['š','č','ž','Š','Č','Ž','ć','Ć']
    nesumniki=['s','c','z','S','C','Z','c','C']
    a=''
    for i in niz:
        if i in sumniki:
            a+=nesumniki[sumniki.index(i)]
        else:
            a+=i
    return a
def presledki(niz):
    a=''
    for i in niz:
        if i!=' ':
            a+=i
    return a


def izracunLigeA(rezultatiTekme,st_tekme,stanjeLigeA,IP=1):
    #'st_tekme' je št ZL(npr. pri ZL2, je to 2).
    #IP je vrednost tekme(1.2 pomeni, da je tekmo vredna 20 % več).
    if rezultatiTekme:
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
        for (a,b) in rezultatiTekme.keys():
            x=sumniki(a)
            y=sumniki(b)
            if stanjeLigeA[(x,y)][0][1]>600:
                seznamTock.append(stanjeLigeA[(x,y)][0][1])
                if rezultatiTekme[(a,b)]!='mp':
                    seznamCasov.append((rezultatiTekme[(a,b)][0])*3600+(rezultatiTekme[(a,b)][1])*60+rezultatiTekme[(a,b)][2])
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
                stanjeLigeA[(sumniki(x),sumniki(y))][st_tekme]=[rezultatiTekme[(x,y)],round(RP),mesto]
            else:
                stanjeLigeA[(sumniki(x),sumniki(y))][st_tekme]=['mp','-']
            vsota_=0
            k=0
            for i,j in stanjeLigeA[(x,y)].items():
                if i not in ['sestevek','povprecje','klub','ime','priimek'] and j[1]!='-' and j[1]>0:
                    vsota_+=round(j[1])
                    k+=1
                else:
                    pass
            if k!=0:
                stanjeLigeA[(sumniki(x),sumniki(y))][0]=[0,round(vsota_/k)]

        #Računamo skupni seštevek lige.
        for x,y in stanjeLigeA:
            seznam=[]
            for i,j in stanjeLigeA[(x,y)].items():
                if i in [k for k in range(1,20)] and j[1]!='-' and j[1]>0:
                    seznam.append(j[1])
            seznam.sort()
            seznam=seznam[::-1]
            if len(seznam)==0:
                pass
            elif len(seznam)>=4:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:4])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:4])/4)
            else:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:len(seznam)])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:len(seznam)])/len(seznam))
    return stanjeLigeA



def izracunLigeB(rezultatiTekme,st_tekme,stanjeLigeB={},IP=1):
    if rezultatiTekme:
        #Sestavljamo seznam z časi.
        seznamCasov=[]
        for (x,y) in rezultatiTekme.keys():
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
            
                stanjeLigeB[(sumniki(x),sumniki(y))][st_tekme]=[rezultatiTekme[(x,y)],round(3*((len(seznamCasov)-mesto+1+100*casNajboljsega/((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]))*IP)),mesto]
            else:
                stanjeLigeB[(sumniki(x),sumniki(y))][st_tekme]=['mp','-']
                
        #Računamo skupni seštevek lige.
        stanjeLigeA=stanjeLigeB
        for x,y in stanjeLigeA:
            seznam=[]
            for i,j in stanjeLigeA[(x,y)].items():
                if i in [k for k in range(1,20)] and j[1]!='-':
                    seznam.append(j[1])
            seznam.sort()
            seznam=seznam[::-1]
            if len(seznam)==0:
                pass
            elif len(seznam)>=4:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:4])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:4])/4)
            else:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:len(seznam)])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:len(seznam)])/len(seznam))
        return stanjeLigeA
    else:
        return stanjeLigeB



def izracunLigeC(rezultatiTekme,st_tekme,stanjeLigeC={},IP=1):
    if rezultatiTekme:
        stanjeLigeB=stanjeLigeC
        #Sestavljamo seznam z časi.
        seznamCasov=[]
        for (x,y) in rezultatiTekme.keys():
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
                stanjeLigeB[(sumniki(x),sumniki(y))][st_tekme]=[rezultatiTekme[(x,y)],round((len(seznamCasov)-mesto+1+100*casNajboljsega/((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]))*IP),mesto]
            else:
                stanjeLigeB[(sumniki(x),sumniki(y))][st_tekme]=['mp','-']
                
        #Računamo skupni seštevek lige.
        stanjeLigeA=stanjeLigeB
        for x,y in stanjeLigeA:
            seznam=[]
            for i,j in stanjeLigeA[(x,y)].items():
                if i in [k for k in range(1,20)] and j[1]!='-':
                    seznam.append(j[1])
            seznam.sort()
            seznam=seznam[::-1]
            if len(seznam)==0:
                pass
            elif len(seznam)>=4:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:4])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:4])/4)
            else:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:len(seznam)])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:len(seznam)])/len(seznam))
        return stanjeLigeA
    else:
        return stanjeLigeC



def rezultati(st_lige,stanjeLige):
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
                a=True
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
                        if col==''or col =='\"\"':
                            cas1=False
                        else:
                            cas1=col
                    elif header[colnum]=='Cl.name':
                        klub=col
                    elif header[colnum]=='Classifier':
                        ok=col
                    else:
                        pass            
                    colnum+=1
                ok=int(ok)
                if cas1==False or ok in [1,2,3,4]:
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
                if cas!='mp':
                    for i in range(2,0,-1):
                        if cas[i]>=60:
                            cas[i-1]=cas[i-1]+cas[i]//60
                            cas[i]=cas[i]%60                       
                a=''
                for i in klub:
                    if i.isalpha() or i==' ':
                        a+=i
                klub=a
                
                a=''
                b=0
                for i in ime:
                    if i.isalpha():
                        if b==0:
                            i=i.upper()
                        a+=i
                    b+=1
                ime=a
                a=''
                b=0
                for i in ime:
                    if i.isupper()and b!=0:
                        a+=' '
                        a+=i
                    else:
                        a+=i
                    b+=1
                ime=a
                a=''
                b=0
                for i in priimek:
                    if i.isalpha():
                        if b==0:
                            i=i.upper()
                        a+=i
                    b+=1
                priimek=a
                a=''
                b=0
                for i in priimek:
                    if i.isupper() and b!=0:
                        a+=' '
                        a+=i
                    else:
                        a+=i
                    b+=1
                priimek=a
                a=''
                for i in kategorija:
                    if i!='"':
                        a+=i
                kategorija=a
                ime1=sumniki(ime)
                priimek1=sumniki(priimek)
                klub1=klub
                if ime1=='Nejc'and priimek1=='Zorman':
                    ime1='Jernej'
                a={'scommendrisio':'SCOM Mendriso','rodjezerskizmaj':'RJZ Velenje','ind':'ind.','ssdgaja':'SSD Gaja','okkomenda':'OK Komenda','pdajdovscina':'PD Ajdovščina','okazimut':'OK Azimut', 'okbrezice':'OK Brežice','okperkmandeljc':'OK Perkmandeljc','okpolaris':'OK Polaris','okslovenjgradec':'OK Slovenj Gradec','okslovenskekonjice':'OK Slovenske Konjice','oktivoli':'OK Tivoli','oktrzin':'OK Trzin','rjzvelenje':'RJZ Velenje','sok':'ŠOK'}
                if presledki(sumniki(klub1).lower()) in a.keys():
                    klub1=a[presledki(sumniki(klub1).lower())]
                if kategorija== "A":
                    if (ime1,priimek1) not in stanjeLige['A']:
                        stanjeLige['A'][(ime1,priimek1)]={0:[0,500],'ime':ime,'priimek':priimek,'klub':klub1}
                    elif stanjeLige['A'][(ime1,priimek1)].get('klub',1)==(1 or '' or 'ind.' or ' '):
                        if klub1==(' 'or''or'ind'):
                            klub1=='ind.'
                        stanjeLige['A'][(ime1,priimek1)]['klub']=klub1                     
                    rezultatiTekmeA[(ime1,priimek1)]=cas
                elif kategorija== "B":
                    if (ime1,priimek1) not in stanjeLige['B']:
                        stanjeLige['B'][(ime1,priimek1)]={'ime':ime,'priimek':priimek,'klub':klub1}
                    elif stanjeLige['B'][(ime1,priimek1)].get('klub',1)==(1 or '' or 'ind.' or ' '):
                        if klub1==(' 'or''or'ind'):
                            klub1=='ind.'
                        stanjeLige['B'][(ime1,priimek1)]['klub']=klub1
                    rezultatiTekmeB[(ime1,priimek1)]=cas
                elif kategorija== "C":
                    if (ime1,priimek1) not in stanjeLige['C']:
                        stanjeLige['C'][(ime1,priimek1)]={'ime':ime,'priimek':priimek,'klub':klub1}
                    elif stanjeLige['C'][(ime1,priimek1)].get('klub',1)==(1 or '' or 'ind.' or ' '):
                        if klub1==(' 'or''or'ind'):
                            klub1=='ind.'
                        stanjeLige['C'][(ime1,priimek1)]['klub']=klub1
                    rezultatiTekmeC[(ime1,priimek1)]=cas
                else:
                    pass
            rownum+=1
    rezultatiTekme={'A':rezultatiTekmeA,'B':rezultatiTekmeB,'C':rezultatiTekmeC}
    return rezultatiTekme
def vCsv(stanjeLige,st_tekem):
    with open('./Stanja_racunana/StanjeLige'+str(st_tekem)+'.csv','w+',encoding='utf-8') as f:
        f.write('Surname;First name;Cl.name;Class;Time;Pl;Points')
        for i in range(1,st_tekem +1):
            f.write(';'+'ZL'+str(i))
        f.write(';Sum;Average\n')
        for k in ['A','B','C']:
            h=[]
            for x,y in stanjeLige[k].keys():
                if stanjeLige[k][x,y].get('sestevek',None)!=None:
                    h.append((stanjeLige[k][x,y]['sestevek'],stanjeLige[k][x,y]['povprecje'],x,y))
            h.sort()
            h=h[::-1]
            for t,z,x,y in h:
                if stanjeLige[k][x,y].get('klub',None)!=None:
                    if stanjeLige[k][x,y].get('sestevek',None)==None:
                            pass
                    elif stanjeLige[k][x,y].get(st_tekem,None)==None:
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+str(stanjeLige[k][x,y]['klub'])+';'+k+';'+''+';'+''+';'+'')
                    elif stanjeLige[k][x,y][st_tekem][0]!='mp':
                        cas=''
                        podpicja=0
                        for j in range(3):
                            for i in str(stanjeLige[k][x,y][st_tekem][0][j]):
                                if len(str(stanjeLige[k][x,y][st_tekem][0][j]))<2 and j!=0:
                                    cas+='0'
                                cas+=i
                            podpicja+=1
                            if podpicja!=3:
                                    cas+=':'
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+str(stanjeLige[k][x,y]['klub'])+';'+k+';'+cas+';'+str(stanjeLige[k][x,y][st_tekem][2])+';'+str(stanjeLige[k][x,y][st_tekem][1]))
                    else:
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+str(stanjeLige[k][x,y]['klub'])+';'+k+';'+'mp'+';'+''+';'+'')
                    if stanjeLige[k][x,y].get('sestevek',None)!=None:
                        for i in range(1,st_tekem +1):
                            if stanjeLige[k][x,y].get(i,None)!=None:
                                f.write(';'+str(stanjeLige[k][x,y][i][1]))
                            else:
                                f.write(';'+'')
                        f.write(';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')

                else:
                    if stanjeLige[k][x,y].get('sestevek',None)==None:
                            pass
                    elif stanjeLige[k][x,y].get(st_tekem,None)==None:
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+''+';'+k+';'+''+';'+''+';'+'')
                    elif stanjeLige[k][x,y][st_tekem][0]!='mp':
                        cas=''
                        podpicja=0
                        for j in range(3):
                            for i in str(stanjeLige[k][x,y][st_tekem][0][j]):
                                cas+=i
                            podpicja+=1
                            if podpicja!=3:
                                cas+=':'
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+''+';'+k+';'+str(cas)+';'+str(stanjeLige[k][x,y][st_tekem][2])+';'+str(stanjeLige[k][x,y][st_tekem][1]))
                    else:
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+''+';'+k+';'+'mp'+';'+''+';'+'')
                    if stanjeLige[k][x,y].get('sestevek',None)!=None:
                        for i in range(1,st_tekem +1):
                            if stanjeLige[k][x,y].get(i,None)!=None:
                                f.write(';'+str(stanjeLige[k][x,y][i][1]))
                            else:
                                f.write(';'+'')
                        f.write(';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')

