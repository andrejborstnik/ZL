indeksi=[] #V indeksi zapiši zaporedne številke tekem, pri katereih točke
#ne štejejo v povprečje za računanje novih rezultatov.

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
            else:
                return 0
        
        def standardnaDeviacija(seznam):
            #Iz seznama točk/časov tekmovalccev izračuna standardno deviacijo.
            if seznam:
                Povprecje=povprecje(seznam)
                vsota=0
                for x in seznam:
                    vsota+=(Povprecje-x)**2
                standardnaDeviacija=(vsota/len(seznam))**0.5
                return standardnaDeviacija
            else:
                return 0
            
        #Sestavljamo seznam z časi in točkami.
        seznamCasov=[]
        seznamTock=[]
        #print(rezultatiTekme)
        for (a,b) in rezultatiTekme.keys():
            x=sumniki(a)
            y=sumniki(b)
            #print(stanjeLigeA[(x,y)][0][1])
            if stanjeLigeA[(x,y)][0][1]>600:
                seznamTock.append(stanjeLigeA[(x,y)][0][1])
                if rezultatiTekme[(a,b)]not in ['mp','dns']:
                    seznamCasov.append((rezultatiTekme[(a,b)][0])*3600+(rezultatiTekme[(a,b)][1])*60+rezultatiTekme[(a,b)][2])
        #Računamo točke(glej formulo na iof strani) in zapisujemo rezultat/tocke/mesto.
        ST=standardnaDeviacija(seznamCasov)
        SP=standardnaDeviacija(seznamTock)
        if not SP:
            SP = 1
        MT=povprecje(seznamCasov)
        MP=povprecje(seznamTock)
        if not MP:
            MP = 600
        #print(seznamCasov,MT)
        seznamCasov=[]
        for (x,y) in rezultatiTekme.keys():
            if rezultatiTekme[(x,y)]not in ['mp','dns']:
                seznamCasov.append((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2])
        if ST == 0:
            ST = standardnaDeviacija(seznamCasov)
        seznamCasov.sort()
        for x,y in rezultatiTekme.keys():
            if rezultatiTekme[(x,y)]not in ['mp','dns']:
                RT=(rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]
                for i in range(len(seznamCasov)):
                    if seznamCasov[i]==RT:
                        mesto=i+1
                        break
                RP=(MP+SP*(MT-RT)/ST)*IP
                stanjeLigeA[(sumniki(x),sumniki(y))][st_tekme]=[rezultatiTekme[(x,y)],round(RP),mesto]
            else:
                stanjeLigeA[(sumniki(x),sumniki(y))][st_tekme]=[rezultatiTekme[(x,y)],'-']
            
            
            if stanjeLigeA[(sumniki(x),sumniki(y))][0][2]:#Naj ostanejo točke iz začetka leta, če obstajajo (tam je true/false), sicer zračunamo povprečje.
                #k=0
                l=0
                #vsota_=0
                vsota2=0 #Vsota za povprečje.
                for i,j in stanjeLigeA[(x,y)].items():
                    if i not in ['sestevek','povprecje','klub','ime','priimek'] and j[1]!='-' and j[1]>0:
                        #vsota_+=round(j[1])
                        if i not in indeksi:
                            vsota2+=round(j[1])
                            l+=1
                        #k+=1
                    else:
                        pass
                if l!=0:
                    stanjeLigeA[(sumniki(x),sumniki(y))][0]=[0,round(vsota2/l),True]

            
        #Računamo skupni seštevek lige.
        for x,y in stanjeLigeA:
            seznam=[]
            for i,j in stanjeLigeA[(x,y)].items():
                if i in [k for k in range(1,st_tekme+1)] and j[1]!='-' and j[1]>0:
                    seznam.append(j[1])
            seznam.sort()
            seznam=seznam[::-1]
            if len(seznam)==0:
                pass
            elif len(seznam)>=5:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:5])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:5])/5)
                ##stanjeLigeA[(x,y)][0][1] = max(stanjeLigeA[(x,y)]['povprecje'],stanjeLigeA[(x,y)][0][1])
            else:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:len(seznam)])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:len(seznam)])/len(seznam))
                ##stanjeLigeA[(x,y)][0][1] = max(stanjeLigeA[(x,y)]['povprecje'],stanjeLigeA[(x,y)][0][1])
    return stanjeLigeA



def izracunLigeB(rezultatiTekme,st_tekme,stanjeLigeB={},IP=1):
    if rezultatiTekme:
        #Sestavljamo seznam z časi.
        seznamCasov=[]
        for (x,y) in rezultatiTekme.keys():
            if rezultatiTekme[(x,y)]not in ['mp','dns']:                  
                seznamCasov.append((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2])
        casNajboljsega=min(seznamCasov)
        seznamCasov.sort()
        seznamCasov=seznamCasov[::-1]
        for (x,y) in rezultatiTekme.keys():
            if rezultatiTekme[(x,y)]not in ['mp','dns']:
                for i in range(len(seznamCasov)):
                    if seznamCasov[i]==(rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]:
                        mesto=len(seznamCasov)-i
                        break
                thisRez = (rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]
                if thisRez <= 0:
                    thisRez = thisRez / casNajboljsega
                else:
                    thisRez = casNajboljsega / thisRez
                stanjeLigeB[(sumniki(x),sumniki(y))][st_tekme]=[rezultatiTekme[(x,y)],
                                                                round(3*((len(seznamCasov)-mesto+1+100*thisRez)*IP)),mesto]
            else:
                stanjeLigeB[(sumniki(x),sumniki(y))][st_tekme]=[rezultatiTekme[(x,y)],'-']
                
        #Računamo skupni seštevek lige.
        stanjeLigeA=stanjeLigeB
        for x,y in stanjeLigeA:
            seznam=[]
            for i,j in stanjeLigeA[(x,y)].items():
                if i in [k for k in range(1,st_tekme+1)] and j[1]!='-':
                    seznam.append(j[1])
            seznam.sort()
            seznam=seznam[::-1]
            if len(seznam)==0:
                pass
            elif len(seznam)>=5:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:5])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:5])/5)
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
            if rezultatiTekme[(x,y)]not in ['mp','dns']:
                seznamCasov.append((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2])
        casNajboljsega=min(seznamCasov)
        seznamCasov.sort()
        seznamCasov=seznamCasov[::-1]
        for (x,y) in rezultatiTekme.keys():
            if rezultatiTekme[(x,y)]not in ['mp','dns']:
                for i in range(len(seznamCasov)):
                    if seznamCasov[i]==(rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]:
                        mesto=len(seznamCasov)-i
                        break
                stanjeLigeB[(sumniki(x),sumniki(y))][st_tekme]=[rezultatiTekme[(x,y)],round((len(seznamCasov)-mesto+1+100*casNajboljsega/((rezultatiTekme[(x,y)][0])*3600+(rezultatiTekme[(x,y)][1])*60+rezultatiTekme[(x,y)][2]))*IP),mesto]
            else:
                stanjeLigeB[(sumniki(x),sumniki(y))][st_tekme]=[rezultatiTekme[(x,y)],'-']
                
        #Računamo skupni seštevek lige.
        stanjeLigeA=stanjeLigeB
        for x,y in stanjeLigeA:
            seznam=[]
            for i,j in stanjeLigeA[(x,y)].items():
                if i in [k for k in range(1,st_tekme+1)] and j[1]!='-':
                    seznam.append(j[1])
            seznam.sort()
            seznam=seznam[::-1]
            if len(seznam)==0:
                pass
            elif len(seznam)>=5:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:5])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:5])/5)
            else:
                stanjeLigeA[(x,y)]['sestevek']=sum(seznam[0:len(seznam)])
                stanjeLigeA[(x,y)]['povprecje']=round(sum(seznam[0:len(seznam)])/len(seznam))
        return stanjeLigeA
    else:
        return stanjeLigeC



def rezultati(st_lige,stanjeLige):
    #Vrne rezultate tekme v slovarju oblike {'A':rezultatiTekmeA,...}.
    rezultatiTekmeA={0: {}}
    rezultatiTekmeB={}
    rezultatiTekmeC={}
    import csv
    kodiranje='utf-8'
    score = False
    with open('./Rezultati/ZL'+str(st_lige)+'.csv',encoding=kodiranje) as f:
        reader=csv.reader(f)
        rownum=0
        for row in reader:
            if rownum==0:
                header=str(row[0]).split(';')
                #print(header)
            elif rownum==0:
                pass
            else:
                colnum=0
                a=True
                g=True
                for col in row[0].split(';'):
                    if colnum>=len(header):
                        break
                    if header[colnum]=='First name':
                        ime=col
                    elif header[colnum]=='Surname' or header[colnum][1:] == "Surname":
                        priimek=col
                    elif header[colnum]=='Short':
                        kategorija=col
                    elif header[colnum]=='Time':
                        if col==''or col =='\"\"' or col in ['mp']:
                            cas='mp'
                            cas1=False
                        elif col in ['dns']:
                            cas='dns'
                            cas1=False
                        else:
                            cas1=col
                    elif header[colnum]=='City':
                        if g:
                            klub=col
                            g=False
                    elif header[colnum]=='Classifier':
                        ok=col
                    else:
                        pass            
                    colnum+=1
                # checking if ok exists
                try:
                    ok #try
                except:
                    ok = ""

                if ok == "":
                    ok = 0
                else:
                    ok=int(ok)
                if 'cas1' in vars():
                    if ok in [2,3,4]:
                        cas='mp'
                    elif ok==1:
                        cas='dns'
                    elif not cas1 == False:
                        

                        if not ':' in cas1:
                            cas = [0,0,-abs(float(cas1))]
                            if score == False:
                                score = True
                                print("Vklopljen score na tekmi {0}.".format(st_lige))
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
                
                if ('cas1' in vars()) and cas not in ['mp','dns'] and len(cas) > 1:
                    for i in range(2,0,-1):
                        if cas[i]>=60:
                            cas[i-1]=cas[i-1]+cas[i]//60
                            cas[i]=cas[i]%60
                a=''
                try:
                    klub
                except:
                    klub = []
                for i in klub:
                    if i.isalpha() or i==' ':
                        a+=i
                klub=a
                
                a=''
                b=0
                try:
                    ime
                except:
                    ime = []
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
                try:
                    priimek
                except: 
                    priimek = []
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
                try:
                    kategorija
                except:
                    kategorija = []
                for i in kategorija:
                    if i!='"':
                        a+=i
                kategorija=a
                ime1=sumniki(ime)
                priimek1=sumniki(priimek)
                klub1=klub
                if ime1=='Nejc'and priimek1=='Zorman':
                    ime1='Jernej'
                elif priimek=='Rejec':
                    klub1='OK Azimut'
                elif ime1=='Ivo'and priimek1=='Kette':
                    priimek1='Kete'
                if ime1 == "Anapia":
                    ime1 = "Ana Pia"
##                elif priimek == "Kacin":
##                    print(klub)
##                elif priimek == "Plavčak":
##                    print(klub)
                #print(ime, priimek, klub)
                a={'semiperdoorienteeringmaniagosemiperdomaniago':'Semiperdo Orienteering Maniago','mokmariborskiok':'Mariborski OK','kamniskiokkokkamniskiorientacijskiklub': 'Kamniški OK','scommendrisio':'SCOM Mendriso','rodjezerskizmaj':'RJZ Velenje','ssdgaja':'SSD Gaja','orientacijskiklubkomendaokkomenda':'OK Komenda','pdajdovscinaplaninskodrustvoajdovscina':'PD Ajdovščina','orientacijskiklubazimutokazimut':'OK Azimut', 'orientacijskiklubbreziceokbrezice':'OK Brežice','orientacijskiklubperkmandeljcokperkmandeljc':'OK Perkmandeljc','orientacijskiklubpolarisokpolaris':'OK Polaris','orientacijskiklubslovenjgradecokslovenjgradec':'OK Slovenj Gradec','orientacijskiklubslovenskekonjiceokslovenskekonjice':'OK Slovenske Konjice','orientacijskiklubtivolioktivoli':'OK Tivoli','orientacijskiklubtrzinoktrzin':'OK Trzin','rjzvelenje':'RJZ Velenje','sokskofjeloskiokskofjeloskiorientacijskiklub':'ŠOK'}
                ind=[' ','','ind','ind.','individual','Individuals/No Club', 'IndividualsNo Club', 'IndividualsNo club', 'Individual', 'Individuals']
                if sumniki(klub1).lower() == "sok":
                    klub1 = "ŠOK"
                else:
                    for kl in a.keys():
                        if presledki(sumniki(klub1).lower()) in kl and presledki(sumniki(klub1).lower()):
                            klub1=a[kl]
                            break
                if kategorija[0]== "A": ## will allow for multiple categories merged into A
                    if klub1 in ind:
                        klub1='ind.'       
                    if (ime1,priimek1) not in stanjeLige['A'].keys():
                        stanjeLige['A'][(ime1,priimek1)]={0:[0,500,True],'ime':ime,'priimek':priimek,'klub':klub1}
                    elif stanjeLige['A'][(ime1,priimek1)].get('klub',1)in [1,' ','','ind','ind.']:
                        stanjeLige['A'][(ime1,priimek1)]['klub']=klub1
                    if cas!='dns':
                        if len(kategorija) == 1:
                            kje = 0
                        else:
                            kje = int(kategorija[1:])
                        if kje > 0 and rezultatiTekmeA.get(kje, None) == None:
                            rezultatiTekmeA[kje] = {}
                        rezultatiTekmeA[kje][(ime1,priimek1)] = cas ## will allow for multiple categories merged into A
                elif kategorija== "B":
                    if klub1 in ind:
                        klub1='ind.'
                    if (ime1,priimek1) not in stanjeLige['B']:
                        stanjeLige['B'][(ime1,priimek1)]={'ime':ime,'priimek':priimek,'klub':klub1}
                    elif stanjeLige['B'][(ime1,priimek1)].get('klub',1)in [1,' ','','ind','ind.']:
                        stanjeLige['B'][(ime1,priimek1)]['klub']=klub1
                    ###Bonus za d...
                    elif priimek=='Rejec':
                        stanjeLige['B'][(ime1,priimek1)]['klub']=klub1
                    ###
                    if cas!='dns':
                        rezultatiTekmeB[(ime1,priimek1)]=cas
                elif kategorija== "C":
                    if klub1 in ind:
                        klub1='ind.'
                    if (ime1,priimek1) not in stanjeLige['C']:
                        stanjeLige['C'][(ime1,priimek1)]={'ime':ime,'priimek':priimek,'klub':klub1}
                    elif stanjeLige['C'][(ime1,priimek1)].get('klub',1)in [1,' ','','ind','ind.']: 
                        stanjeLige['C'][(ime1,priimek1)]['klub']=klub1
                    if cas!='dns':
                        rezultatiTekmeC[(ime1,priimek1)]=cas
                else:
                    pass
            rownum+=1
    rezultatiTekme={'A':rezultatiTekmeA,'B':rezultatiTekmeB,'C':rezultatiTekmeC}
    return rezultatiTekme, score
def vCsv(stanjeLige,st_tekem, score = False):
    with open('./Stanja_racunana/StanjeLige'+str(st_tekem)+'.csv','w+',encoding='utf-8') as f:
        f.write('Surname;First name;City;Class;Time;Pl;Points')
        for i in range(1,st_tekem +1):
            f.write(';'+'ZL'+str(i))
        f.write(';Sum;Average\n')
        for k in ['A','B','C']:
            h=[]
            for x,y in stanjeLige[k].keys():
                if stanjeLige[k][x,y].get('sestevek',None)!=None:
                    h.append((stanjeLige[k][x,y]['sestevek'],stanjeLige[k][x,y]['povprecje'],x,y))
                else:
                    h.append((0,0,x,y))
            h.sort()
            h=h[::-1]
            for t,z,x,y in h:
                if stanjeLige[k][x,y].get('klub',None)!=None:
                    try:
                        a=stanjeLige[k][x,y][st_tekem]
                    except:a=False
                    if stanjeLige[k][x,y].get('sestevek',None)==None and not a:
                        pass
                    elif stanjeLige[k][x,y].get(st_tekem,None)==None:
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+str(stanjeLige[k][x,y]['klub'])+';'+k+';'+''+';'+''+';'+'')
                    elif stanjeLige[k][x,y][st_tekem][0] not in ['mp','dns']:
                        if score: ## and k != "C":
                            cas = str(abs(stanjeLige[k][x,y][st_tekem][0][2]))
                        else:
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
                    elif stanjeLige[k][x,y][st_tekem][0]=='mp':
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+str(stanjeLige[k][x,y]['klub'])+';'+k+';'+stanjeLige[k][x,y][st_tekem][0]+';'+''+';'+'')
                    if stanjeLige[k][x,y].get('sestevek',None)!=None or a:
                        for i in range(1,st_tekem +1):
                            if stanjeLige[k][x,y].get(i,None)!=None:
                                f.write(';'+str(stanjeLige[k][x,y][i][1]))
                            else:
                                f.write(';'+'')
                        if stanjeLige[k][x,y].get('sestevek',None)!=None:
                            f.write(';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')
                        else:
                            f.write(';'+str(0)+';'+str(0)+'\n')

                else:
                    try:
                        a=stanjeLige[k][x,y][st_tekem]
                    except:a=False
                    if stanjeLige[k][x,y].get('sestevek',None)==None and not a:
                            pass
                    elif stanjeLige[k][x,y].get(st_tekem,None)==None:
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+''+';'+k+';'+''+';'+''+';'+'')
                    elif stanjeLige[k][x,y][st_tekem][0]!='mp':
                        if score: ## and k != "C":
                            cas = stanjeLige[k][x,y][st_tekem][0][2]
                        else:
                            cas=''
                            podpicja=0
                            for j in range(3):
                                for i in str(stanjeLige[k][x,y][st_tekem][0][j]):
                                    cas+=i
                                podpicja+=1
                                if podpicja!=3:
                                    cas+=':'
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+''+';'+k+';'+str(cas)+';'+str(stanjeLige[k][x,y][st_tekem][2])+';'+str(stanjeLige[k][x,y][st_tekem][1]))
                    elif stanjeLige[k][x,y][st_tekem][0]=='mp':
                        f.write(stanjeLige[k][x,y]['priimek']+';'+stanjeLige[k][x,y]['ime']+';'+''+';'+k+';'+stanjeLige[k][x,y][st_tekem][0]+';'+''+';'+'')
                    if stanjeLige[k][x,y].get('sestevek',None)!=None or a:
                        for i in range(1,st_tekem +1):
                            if stanjeLige[k][x,y].get(i,None)!=None:
                                f.write(';'+str(stanjeLige[k][x,y][i][1]))
                            else:
                                f.write(';'+'')
                        if stanjeLige[k][x,y].get('sestevek',None)!=None:
                            f.write(';'+str(stanjeLige[k][x,y]['sestevek'])+';'+str(stanjeLige[k][x,y]['povprecje'])+'\n')
                        else:
                            f.write(';'+str(0)+';'+str(0)+'\n')

