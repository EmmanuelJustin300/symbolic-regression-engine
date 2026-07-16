import expression_tree as eqn
import random
import os
import math

"""Need a way to check if eqn if valid to write into file,
remove all constant graphs too,
then loop create datasets for comparison"""

def gen_data(equation):
  
    data = []
    for i in range(random.randint(20,70)):
        x = random.uniform(-10, 10)
        y = equation.evaluate(x)
        data.append((x, y))
        data.sort(key=lambda point: point[0])

    for each in data:
        print(f"({each[0]}, {each[1]})\n")

    return data



def gen_file_name():
    i=1
    while os.path.exists(f"Data/dataset_{i:05}.txt"):
        i += 1

    return (f"Data/dataset_{i:05}.txt")



def check_valid(equation, data):

    if any(math.isnan(y) for x,y in data):
        print("nan present")
        return False
    
    if str(equation) == "x":
        return False
    
    #Check for y value not changing
    const_y = True
    for (x1,y1),(x2,y2) in zip(data, data[1:]):
        if y1 != y2:
            const_y = False
    if const_y == True:
        print("Y VALUE NOT CHANGING")
        return False
    
    
    try:
        float(str(equation))
        print("constant equation")
        return False
    except ValueError:
        pass

    return True
    



def gen_file():
    equation = eqn.ExpressionTree(3)
    data = gen_data(equation)
    filename = gen_file_name()
    


    print(equation)
    print(filename)

    if check_valid(equation, data):
        with open(filename, "x") as f:
            f.write(f"f(x)={str(equation)}\n")
            for each in data:
                f.write(f"{each[0]:.3f}, {each[1]:.3f}\n")
        f.close
    else:
        return
    

for each in range(10):
    try:
        gen_file()
    except:
        continue