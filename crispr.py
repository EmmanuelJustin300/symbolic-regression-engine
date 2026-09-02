import expression_tree as eqn
import random

#make way to get node id's
#fix up how confusing it is cuz printing a node as a string comes with all its kids
#but get_value prints just the node and thats not very clear


equation = eqn.Expression.random(6)
print("equation: " + str(equation))
#print(str(equation))

list1 = ["a", "b", "c", "d"]

def delete_list_value(list, value): 
    list.remove(value)
    return list


#print(delete_list_value(list1,"a"))

def get_first_child(expression):
    if isinstance(expression.root, eqn.UnaryNode):
        print("Unary Node, child is " + str(expression.root.child))
        return expression.root.child
    elif isinstance(expression.root, eqn.BinaryNode):
        print("Binary Node, left child is " + str(expression.root.left))
        print("Binary Node, right child is " + str(expression.root.right))
    else:
        print("VALUE NODE: " + str(expression.root))


    



#left_node = get_first_child(equation)     



def get_random_node(expression):
    node_list = expression.offspring(expression.root)
    return random.choice(node_list)

print("The node selected has a value of: " + get_random_node(equation).get_value())


def delete_node_ish(expression, node):
    if expression.root is node:
        return expression
    elif isinstance(expression.root, eqn.UnaryNode):



def delete_node_eman(expression, node):
    return


def find_node(expression, node):
    if expression.root is node:
        return True
    elif isinstance(expression.root, eqn.ValueNode):
        return False
    elif isinstance(expression.root, eqn.UnaryNode):
        find_node(eqn.Expression(expression.root.child))
    elif isinstance(expression.root, eqn.BinaryNode):
        find_node()

