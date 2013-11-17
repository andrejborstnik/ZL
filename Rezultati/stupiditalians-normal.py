def pretvori(niz):
    niz1=niz.split(' ')
    b=''
    for niz in niz1:
        b+=niz[0]+niz[1:].lower()+' '
    return b[:-1]
with open('ZL10.txt','r',encoding='utf-8') as f:
    with open('ZL10.csv','w',encoding='utf-8')as g:
        kat='A'
        g.write('@SI\n')
        g.write('Pl;First name;Surname;Time;Short;City;Classifier;\n')
        for i in f:
            a=i.split(';')
            if i!='\n':
                ime=''
                for k in a[3].split(' ')[1:]:
                    ime+=k+' '
                ime=pretvori(ime[:-1])
                priimek=pretvori(a[3].split(' ')[0])
                if a[2][0]=='=':
                    cas='mp'
                    clas='3'
                else:
                    cas=a[2]
                    clas='0'
                klub=a[8]
                mesto=a[0]
                if mesto:
                    mesto+='.'
                if mesto and mesto[0]=='\ufeff':
                    mesto=mesto[1:]
                g.write(mesto+';'+ime+';'+priimek+';'+cas+';'+kat+';'+klub+';'+clas+';\n')
            elif kat=='A':
                kat='B'
            elif kat=='B':
                kat='C'
                
            
