out = []
newScores = []
times = []

with open("ZL17_a.csv", encoding="UTF-8") as f:
    header = False
    i = -2
    for line in f.readlines():
        if not line or line == "\n":
            continue
        if not header and i == -1:
            header = line[:-1].split(";")
            out.append(";".join(header))
            timeI = header.index("Time")
            scoreI = header.index("Score")
        elif i > -1:
            line = line[:-1].split(";")
            time = line[timeI]
            time1 = time.split(':')
            time = int(time1[-1]) + int(time1[-2]) * 60
            if len(time1) > 2:
                time += int(time1[0]) * 3600
            times.append(time)
            if line[scoreI]:
                newScores.append(float(line[scoreI]))
                line[timeI] = '{' + str(i) + '}'
            else:
                i -= 1
            out.append(";".join(line))
        else:
            out.append(line[:-1])
        i += 1

maxTime = max(times)
newScores = [newScores[i] + 1 - times[i] / maxTime for i in range(len(newScores))]

out = "\n".join(out)
out = out.format(*newScores)

g= open("ZL17.csv", 'w', encoding="UTF-8")
g.write(out)
g.close()
