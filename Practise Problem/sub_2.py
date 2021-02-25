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
pizzas = []
for x in f:
  temp = x.strip().split(" ")
  temp.pop(0)

#   each element is a set containing all the ingredients in that pizza
  pizzas.append(set(temp))

g_pizza_ingredients = set()
g_chosen_pizza_ids = set()
g_chosen_pizzas = []
g_max_ingredients = -1
answer = []

for m in range(four):
    while len(g_chosen_pizza_ids) < 4:
        g_pizza_ingredients = set()
        for c_pizza_id in range(len(pizzas)):
            if (c_pizza_id in g_chosen_pizza_ids):
                continue
            else:
                c_chosen_pizza_ingredients = pizzas[c_pizza_id]
                c_diff_ingredients = len(
                    c_chosen_pizza_ingredients.difference(g_pizza_ingredients))
                if c_diff_ingredients >= g_max_ingredients:
                    g_max_ingredients = c_diff_ingredients
                    c_pizza_ingredients = c_chosen_pizza_ingredients
                    c_chosen_pizza_id = c_pizza_id

        g_chosen_pizza_ids.add(c_chosen_pizza_id)
        g_pizza_ingredients = g_pizza_ingredients.union(c_pizza_ingredients)
        # print(g_chosen_pizza_ids)
    answer.append(g_chosen_pizza_ids)
print(answer)
