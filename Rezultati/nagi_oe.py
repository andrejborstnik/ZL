st=0
with open('ZL9.csv','r',encoding='utf8') as f:
    with open ('ZL9a.csv','w',encoding='utf8') as g:
        for j in f:
            if st!=0:
                for i in j:
                    if i==',':
                        g.write(';')
                    
                    else:
                        g.write(i)
                    '''elif i=='\n' and st==1:
                        pass'''
            st+=1
            if st>2:
                st=1
'''st=0
kategorija='A'
st1=0
with open('ZL9a.csv','r',encoding='utf8') as f:
    with open ('ZL9b.csv','w',encoding='utf8') as g:
        g.write('First Name;Surname;Time;Short\n')
        for j in f:
            if st==1:
                st1+=1
                a=j.split(';')
                if a[0]=='':
                    st=0
                else:
                    ime=''
                    priimek=''
                    gz=False
                    for k in a[2][::-1]:
                        if k!=' ' and not gz:
                            ime+=k
                        elif k==' ' and not gz:
                            gz=True
                        elif gz:
                            priimek+=k
                    a0=a[0]
                    if a0=='1.' and kategorija=='A' and st1!=1:
                        kategorija='B'
                    elif a0=='1.' and kategorija=='B':
                        kategorija='C'
                    ime=ime[::-1]
                    priimek=priimek[::-1]
                    g.write(ime+';'+priimek+';'+a[3]+';'+kategorija+'\n')
            st+=1
            if st==2:
                st=0'''
