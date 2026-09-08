import random, math, operator
from abc import ABC, abstractmethod  

#All this needs cleanup and refiling
#Expression needs to be own file, probably same for Nodes
#Decide whats actually relevant and cast rest aside, e.g
#is Expression even relevant or should i have nodes do all the intra
#node operations idk
#Make comments up top for all classes and such and their
#relevant methods
#Maybe make some methods private so I dont use them

def protected_div(a, b):
        if abs(b) < 1e-12:
            return float("nan")
        return a/b

def protected_log(a):
    if a <= 0:
        return float("nan")
    return math.log(a)

def protected_pow(a, b):
    if a < 0 and not b.is_integer():
        return float("nan")

    try:
        return math.pow(a, b)
    except (OverflowError, ValueError):
        return float("nan")

def protected_exp(a):
    try:
        return math.exp(a)
    except OverflowError:
        return float("nan")

def protected_sin(a):
    try:
        return math.sin(a)
    except (ValueError):
        return float("nan")

def protected_cos(a):
    try:
        return math.cos(a)
    except (ValueError):
        return float("nan")

def protected_tan(a):
    try:
        return math.tan(a)
    except (ValueError):
        return float("nan")



class Expression:
    UNARY_OPERATORS = {
        "sin" : protected_sin,
        "cos" : protected_cos,
        "tan" : protected_tan,
        "exp" : protected_exp,
        "log" : protected_log,
    }
    
    BINARY_OPERATORS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": protected_div,
        "^": protected_pow,
    }

    def __init__(self, root):
        if isinstance(root, Expression):
            self.root = root.root
        elif isinstance(root, Node):
            self.root : Node = root

    @classmethod
    def random_exp(cls, depth):
        root = Node.generate_child(depth)
        return cls(root)

    def random_node(self):
        return random.choice(self.offspring(self.root))


    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self)
    
    def evaluate(self, x):
        try:
            x = float(x)
        except Exception as e:
            print(type(e).__name__)
            print(e)
            return
        
        return self.root.evaluate(x)

    def offspring(self, node):
        nodes = [node]

        for child in node.get_children():
            nodes.extend(self.offspring(child))

        return nodes



class Node(ABC):

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def evaluate(self, x):
        pass

    @abstractmethod
    def get_children(self):
        pass

    def get_value(self):
        pass

    @staticmethod
    def generate_child(depth):

        try:
            depth = int(depth)
        except Exception as e:
            print(type(e).__name__)
            print(e)
            return


        if depth <= 0:
            return ValueNode()
        choice = random.randint(0, 2)

        if choice == 0:
            return ValueNode()
        elif choice == 1:
            return UnaryNode(depth - 1)
        else:
            return BinaryNode(depth - 1)




class ValueNode(Node):
    def __init__(self):
        self.parent: Node = None

        if random.randint(0,1) == 0:
            self.value = "x"
        else:
            if random.random() < 0.7:
                self.value = random.randint(-5, 5)
            else:
                self.value = round(random.uniform(-100, 100), 2)

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return str(self)
    
    
    def evaluate(self, x):
        if self.value == "x":
            return float(x)
        else:
            return float(self.value)


    def get_children(self):
        return []
        


class UnaryNode(Node):
    def __init__(self, depth):
        self.operator = random.choice(list(Expression.UNARY_OPERATORS.keys()))
        self.parent: Node = None

        self.child: Node = Node.generate_child(depth)

        self.child.parent = self


    def __str__(self):
        return self.operator + "(" + str(self.child) + ")"

    def get_value(self):
        return self.operator
    
            
    def evaluate(self, x):
        value = self.child.evaluate(x)

        try:
            return float(Expression.UNARY_OPERATORS[self.operator](value))
        except Exception as e:
            print(f"Failed evaluating: {self.operator}({value})")
            print(f"x = {x}")
            print(f"Error: {e}")
            raise

    def get_children(self):
        return [self.child]
            
            

class BinaryNode(Node):
    def __init__(self, depth):
        self.operator = random.choice(list(Expression.BINARY_OPERATORS.keys()))
        self.parent: Node = None

        self.left: Node = Node.generate_child(depth)
        self.right: Node = Node.generate_child(depth)

        self.left.parent = self
        self.right.parent = self


   
    
    def __str__(self):
        return "(" + str(self.left) + " " + self.operator + " " + str(self.right) + ")"

    def get_value(self):
        return self.operator
            
    def evaluate(self, x):
        leftValue = self.left.evaluate(x)
        rightValue = self.right.evaluate(x)

        return float(Expression.BINARY_OPERATORS[self.operator](leftValue, rightValue))

    def get_children(self):
        return [self.left, self.right]
    print("hello world")


equation = Expression.random_exp(6)
print("equation: " + str(equation))
print(object.__repr__(equation))
random_node = equation.random_node()
print(random_node.get_value())
print("NodeID: " + object.__repr__(random_node))