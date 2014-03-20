with open("registracije.csv","r",encoding = "utf-8")as h:
    reg = str(h.read()).split("\n")
with open('ZL_2013_2014.csv','r',encoding='utf-8')as f:
    with open('zacetek.txt','w',encoding='utf-8')as g:
        b=0
        for i in f.readlines():
            b+=1
            a=0
            if b!=1:
                lol = i.split(";")
                for j in lol:
                    a+=1
                    if a in [1,2,3,4,26]:
                        
                        if a==26:
                            #g.write('\n')
                            g.write(j)
                            pass
                        elif a == 4:
                            nekineki=True
                            for gz in reg:
                                if lol[1] in gz and lol[0] in gz:
                                    g.write(gz.split(";")[4])
                                    g.write(';')
                                    nekineki=False
                                    break
                            if nekineki:
                                g.write("A;")
                        else:
                            g.write(j)
                            g.write(';')
