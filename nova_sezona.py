with open('ZL_2012_2013.csv','r',encoding='utf-8')as f:
    with open('zacetek.txt','w',encoding='utf-8')as g:
        b=0
        for i in f.readlines():
            b+=1
            a=0
            if b!=1:
                for j in i.split(';'):
                    a+=1
                    if a in [1,2,3,4,23]:
                        g.write(j)
                        if a==23:
                            #g.write('\n')
                            pass
                        else:
                            g.write(';')
