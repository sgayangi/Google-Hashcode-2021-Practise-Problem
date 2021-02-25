D,I,S,V,F = map(int,input().split())

streets = dict()
cars = dict()
intersections = []

for i in range(I):
    intersections.append([0]*D)

for i in range(S):
    B,E,name,L=input().split()
    streets[name] = tuple(map(int,[B,E,L]))

for i in range(V):
    P, *ss = input().split()
    P = int(P)
    Tot_L = 0
    for j in ss[1:]:
        Tot_L+=streets[j][2]
    if (P,Tot_L) in cars.keys(): cars[(P,Tot_L)].append(ss)
    else: cars[(P,Tot_L)] = [ss]

index = 0
sorted_cars = sorted(cars.keys())
for current_fastest in sorted_cars:
    for car in cars[current_fastest]:
        time = 0
        for node in car:
            while intersections[streets[node][1]][time]!=0: time+=1
            intersections[streets[node][1]][time] = node
        index+=1

output = []

intersection_id = 0
for inter in intersections:
    notUsed = True
    current_inter = []
    for t in range(D):
        if (inter[t]==0) and notUsed: continue
        elif notUsed:
            notUsed = False
            current_inter.append([inter[t],t+1])
        elif (inter[t]==0) or (inter[t]==current_inter[-1][0]): current_inter[-1][1]+=1
        else: current_inter.append([inter[t],t+1-current_inter[-1][1]])
    if len(current_inter)!=0: output.append([intersection_id]+current_inter)
    intersection_id+=1

print(len(output))
for out in output:
    print(out[0])
    print(len(out)-1)
    for line in out[1:]:
        print(*line)

outfile = open('output.txt', 'w')

outfile.write(str(len(output)))
outfile.write('\n')
for out in output:
    outfile.write(str(out[0]))
    outfile.write('\n')
    outfile.write(str(len(out)-1))
    outfile.write('\n')
    for line in out[1:]:
        outfile.write(line[0] + ' ' + str(line[1]))
        outfile.write('\n')
        outfile.close()
