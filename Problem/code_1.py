input_file = "a"
# a
# b
# c
# d
# e
# f

f = open(r"d:\Programming\Google Hashcode\Problem\Inputs\\"+input_file+".txt", "r")

x = f.readline().split(" ")
Duration = int(x[0])
Intersections_No = int(x[1])
Streets_No = int(x[2])
Cars_No = int(x[3])
Bonus = int(x[4])

intersections = dict()
for i in range(Intersections_No):
    intersections[i] = dict()
    intersections[i]["Incoming Streets"] = []
    intersections[i]["Outgoing Streets"] = []

streets_and_intersections=[]
streets = []
street_names=[]
for i in range(Streets_No):
    B, E, street_name, time = f.readline().split(" ")
    streets.append([street_name, int(time)])
    street_names.append(street_name)
    streets_and_intersections.append([B,E])
    intersections[int(B)]["Incoming Streets"].append(i)
    intersections[int(E)]["Outgoing Streets"].append(i)

cars = []
cars_and_costs =[]
streets_travelled_on = set()
intersections_that_need_to_be_green =set()
for j in range(Cars_No):
    x = f.readline().strip().split(" ")
    x.pop(0)
    cars.append([])
    cost = 0
    for i in range(len(x)):
        s_no = street_names.index(x[i])
        cars[j].append(street_names[s_no])
        intersections_that_need_to_be_green.add(int(streets_and_intersections[s_no][1]))
        streets_travelled_on.add(s_no)
        cost+=(streets[s_no][1])
    cars_and_costs.append(cost)

print(cars)
print(cars_and_costs)

output_file = open(r"d:\Programming\Google Hashcode\Problem\Outputs\\" +input_file+".txt", "w")

