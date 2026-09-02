import expression_tree as eqn
import random
import os
import math


def gen_random_data(equation):
  
    data = []
    for i in range(random.randint(20,70)):
        x = random.uniform(-10, 10)
        y = equation.evaluate(x)
        data.append((x, y))
        data.sort(key=lambda point: point[0])

    """
    for each in data:
        print(f"({each[0]}, {each[1]})\n")

    """

    return data



def gen_file_name():
    i=1
    while os.path.exists(f"Data/dataset_{i:05}.txt"):
        i += 1

    return (f"Data/dataset_{i:05}.txt")



def check_valid(equation, data):

    #Check for all nan values
    if all(math.isnan(y) for x,y in data):
        return False

    return True
    



def gen_file():
    equation = eqn.Expression.random(3)
    data = gen_random_data(equation)
    filename = gen_file_name()
    


    print(equation)
    print(filename)

    if check_valid(equation, data):
        with open(filename, "x") as f:
            f.write(f"f(x)={str(equation)}\n")
            for each in data:
                f.write(f"{each[0]:.3f}, {each[1]:.3f}\n")
    else:
        return


