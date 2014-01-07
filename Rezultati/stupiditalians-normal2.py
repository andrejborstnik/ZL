def pretvori(niz):
    niz1=niz.split(' ')
    b=''
    for niz in niz1:
        if niz not in ['', ' ']:
            b+=niz[0]+niz[1:].lower()+' '
    return b[:-1]
with open('ZL11.csv','r',encoding='utf-8') as f:
    with open('ZL11a.csv','w',encoding='utf-8')as g:
        kat='A'
        g.write('@SI\n')
        g.write('Pl;First name;Surname;Time;Short;City;Classifier;\n')
        z = f.read()
        k=0
        a = z.split('\n')
        for i in a:
            k+=1
            if k > 2:
                b=(i.split(";")[1:])
                s=";".join(b)
                g.write(pretvori(i.split(";")[0])+";"+s+"\n")
                    
            
