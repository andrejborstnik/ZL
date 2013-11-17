with open('ZL_2011_2012.csv','r',encoding='utf-8')as f:
    with open('zacetek.txt','w',encoding='utf-8')as g:
        b=0
        for i in f:
            b+=1
            a=0
            if b!=1:
                for j in i.split(';'):
                    a+=1
                    if a in [1,2,3,4,25]:
                        g.write(j)
                        if a==25:
                            pass#g.write('\n')
                        else:
                            g.write(';')
