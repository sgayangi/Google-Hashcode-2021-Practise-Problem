input_file = "b"
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
    streets.append([street_name, time])
    street_names.append(street_name)
    streets_and_intersections.append([B,E])
    intersections[int(B)]["Incoming Streets"].append(i)
    intersections[int(E)]["Outgoing Streets"].append(i)

cars = []
streets_travelled_on = set()
intersections_that_need_to_be_green =set()
for j in range(Cars_No):
    cars.append([])
    x = f.readline().strip().split(" ")
    x.pop(0)
    for i in range(len(x)):
        s_no = street_names.index(x[i])
        cars[j].append(s_no)
        intersections_that_need_to_be_green.add(int(streets_and_intersections[s_no][1]))
        streets_travelled_on.add(s_no)

# print(streets_travelled_on)
# print(cars)
# print(intersections_that_need_to_be_green)
# print(len(intersections_that_need_to_be_green))
time = int(Duration // len(intersections_that_need_to_be_green))
# print(time)
intersections_that_need_to_be_green = list(intersections_that_need_to_be_green)
print(len(intersections_that_need_to_be_green))

for i in range(len(intersections_that_need_to_be_green)):
    intersection = intersections_that_need_to_be_green[i]
    print(intersection)
    incoming = intersections[intersection]["Incoming Streets"]
    print(len(incoming))
    for road in incoming:
        if road in streets_travelled_on:
            print(street_names[road], end=" ")
            print(time)
    print()

output_file = open(r"d:\Programming\Google Hashcode\Problem\Outputs\\" +input_file+".txt", "w")

