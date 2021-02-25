input_file = "b_little_bit_of_everything"
output_file = input_file+"_output.txt"
# a_example
# b_little_bit_of_everything
# c_many_ingredients
# d_many_pizzas
# e_many_teams
f = open("Inputs/"+input_file+".txt", "r")

x = f.readline().split(" ")
M = int(x[0])
two = int(x[1])
three = int(x[2])
four = int(x[3])
pizzas=[]
for x in f:
  temp = x.strip().split(" ")
  temp.pop(0)

#   each element is a set containing all the ingredients in that pizza
  pizzas.append(set(temp))

iterations = [four, three, two]
ppl = [4, 3, 2]
answer = []
chosen_pizza_ids = []
ingredients_sent = set()