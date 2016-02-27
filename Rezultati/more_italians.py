with open("ZL11b.csv", "r", encoding="utf-8") as f:
    with open("ZL11.csv", "w", encoding="utf-8") as g:
        for i in f.readlines():
            line = i.split(";")
            if len(line) > 5:
                line[5] = line[5].replace(".", ":")
            g.write(";".join(line))
