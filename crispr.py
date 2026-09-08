import expression_tree as eqn
import random

#make way to get node id's
#fix up how confusing it is cuz printing a node as a string comes with all its kids
#but get_value prints just the node and thats not very clear

#Add grab random node function: DONE
#Add delete Node function
#Add add node function
#And then clean up everything and bring back to main

equation = eqn.Expression.random_exp(6)
print("equation: " + str(equation))
print(object.__repr__(equation))
random_node = equation.random_node()
print(random_node.get_value())
print("NodeID: " + object.__repr__(random_node))
