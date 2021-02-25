input_file = "a"
output_file = input_file+"_output.txt"
# a
# b
# c
# d
# e
# f

f = open("Inputs/"+input_file+".txt", "r")

x = f.readline().split(" ")
Duration = int(x[0])
Intersections = int(x[1])
Streets = int(x[2])
Cars = int(x[3])
Bonus = int(x[4])
