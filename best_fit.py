import tkinter as tk
import gen
import expression_tree as eqn
from tkinter.filedialog import askopenfilename
import math


def select_file():
    tk.Tk().withdraw()
    
    filename = askopenfilename()
    print("user chose: ", filename)

    return filename

def grab_data(filename):

    data = []

    with open(filename) as f:
        s = f.read().splitlines()
        equation = s[0]
        for line in s[1:]:
            x, y = line.split(", ")
            x = float(x)
            y = float(y)
            data.append((x,y))


    return(equation, data)


def gen_population(size):
    try:
        size = int(size)
    except:
        size = 50
    population = []
    while len(population) < size:
        equation = eqn.Expression.random(4)

        if gen.check_valid(equation, gen.gen_random_data(equation)):
            population.append(equation)

    return population


def fitness(eqn, training_points):
    total_error = 0.0
    
    for (x,y) in training_points:
        predicted_y = eqn.evaluate(x)
    
        if math.isnan(predicted_y):
            return float('nan')
    
        error = (y - predicted_y)**2
        total_error += error
    mse = total_error / len(training_points)
    return mse




def best_fit():
    population_ranked = []
    initial_equation, points = grab_data(select_file())
    population = gen_population(50)
    print("Chosen Equation: " + str(initial_equation))
    for eqn in population:
        mse = fitness(eqn, points)

        if not math.isnan(mse):
            population_ranked.append((eqn, mse))

    population_ranked = sorted(
        population_ranked,
        key=lambda x: x[1])

    for (eqn, error) in population_ranked:
        print(str(eqn) + "   error: " + str(error))


            

best_fit()
