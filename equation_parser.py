import tkinter as tk
import gen
import expression_tree as eqn
from tkinter.filedialog import askopenfilename
import best_fit as bf


#f(x)=tan((((x * x) + (x + 3)) + (tan(x) * (x * -4.01))))

def run_parse():
    equation, data = bf.grab_data(bf.select_file())
    print(equation)

    parsed_equation = parse(equation)

    return parsed_equation


def parse(equation):
    return


run_parse()