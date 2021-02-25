input_file = "c_many_ingredients"
output_file = input_file+"_output.txt"
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
  pizzas.append(set(temp))
ppl = -1
if four > 0:
    ppl = 4
elif three > 0:
    ppl = 3
elif two > 0:
    ppl = 2

c_pizza_ingredients = set()
c_chosen_pizza_id = -1

g_pizza_ingredients = set()
g_chosen_pizza_ids = set()
g_chosen_pizzas = []
g_max_ingredients = -1

while len(g_chosen_pizza_ids) < ppl:
    g_pizza_ingredients = set()
    for c_pizza_id in range(len(pizzas)):
        if (c_pizza_id in g_chosen_pizza_ids):
            continue
        else:
            c_chosen_pizza_ingredients = pizzas[c_pizza_id]
            c_diff_ingredients = len(c_chosen_pizza_ingredients.difference(g_pizza_ingredients))
            if c_diff_ingredients >= g_max_ingredients:
                g_max_ingredients = c_diff_ingredients
                c_pizza_ingredients = c_chosen_pizza_ingredients
                c_chosen_pizza_id = c_pizza_id

    g_chosen_pizza_ids.add(c_chosen_pizza_id)
    g_pizza_ingredients = g_pizza_ingredients.union(c_pizza_ingredients)
    

to_write = str(ppl)+" "+" ".join(list(map(str,(g_chosen_pizza_ids))))
outF = open(output_file, "w")
outF.write(to_write)
outF.close()
    
