with open('ZL_2016_2017.csv','r',encoding='utf-8')as f:
    with open('zacetek1.txt','w',encoding='utf-8')as g:
        b=0
        for i in f.readlines():
            b+=1
            a=0
            if b!=1:
                for j in i.split(';'):
                    a+=1
                    if a in [1,2,3,4,30]:
                        if a==30:
                            #g.write(str(int(int(j)*1.15)))
                            # naredimo še razteg okoli 1000
                            tocke = int(j[:-1])
                            tocke = int(tocke + (tocke - 1000) * 0.2)
                            g.write(str(tocke))
                            g.write('\n')
                        else:
                            g.write(j)
                            g.write(';')
