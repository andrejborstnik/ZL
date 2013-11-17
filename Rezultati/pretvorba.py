'''with open('ZL14.csv','r+')as f:
    g=open('ZL14a.csv','w+',encoding='utf-8')
    for i in f.readlines():
        b=0
        a=0
        for j in i:
            if b==0:
                g.write(j)
                b+=1
            elif j==';':
                b=0
                a=1
                g.write(j)
            elif a==0:
                g.write(j.lower())
            elif a==1:
                g.write(j.lower())
            else:
                g.write(j)          
    g.close()'''
