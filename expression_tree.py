import random, math, operator
from abc import ABC, abstractmethod  

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



class ExpressionTree:
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

    def __init__(self, depth):

        try:
            x = int(depth)
        except Exception as e:
            print(type(e).__name__)
            print(e)
            return

        self.depth = depth

        match random.randint(0,2):
            case 0:
                self.root = ValueNode()
            case 1:
                self.root = UnaryNode(depth)
            case 2:
                self.root = BinaryNode(depth)

    
    def __str__(self):
        return str(self.root)
    
    def evaluate(self, x):
        try:
            x = float(x)
        except Exception as e:
            print(type(e).__name__)
            print(e)
            return
        
        return self.root.evaluate(x)



class Node(ABC):

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def evaluate(self, x):
        pass

    @staticmethod
    def generate_child(depth):
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
        if random.randint(0,1) == 0:
            self.value = "x"
        else:
            if random.random() < 0.7:
                self.value = random.randint(-5, 5)
            else:
                self.value = round(random.uniform(-100, 100), 2)

    def __str__(self):
        return str(self.value)
    
    
    def evaluate(self, x):
        if self.value == "x":
            return float(x)
        else:
            return float(self.value)
        


class UnaryNode(Node):
    def __init__(self, depth):
        self.operator = random.choice(list(ExpressionTree.UNARY_OPERATORS.keys()))
        self.child: Node = Node.generate_child(depth)

    def __str__(self):
        return self.operator + "(" + str(self.child) + ")"
    
            
    def evaluate(self, x):
        value = self.child.evaluate(x)

        try:
            return float(ExpressionTree.UNARY_OPERATORS[self.operator](value))
        except Exception as e:
            print(f"Failed evaluating: {self.operator}({value})")
            print(f"x = {x}")
            print(f"Error: {e}")
            raise
            
            

class BinaryNode(Node):
    def __init__(self, depth):
        self.operator = random.choice(list(ExpressionTree.BINARY_OPERATORS.keys()))
        self.left: Node = Node.generate_child(depth)
        self.right: Node = Node.generate_child(depth)
    
    def __str__(self):
        return "(" + str(self.left) + " " + self.operator + " " + str(self.right) + ")"
    
            
    def evaluate(self, x):
        leftValue = self.left.evaluate(x)
        rightValue = self.right.evaluate(x)

        return float(ExpressionTree.BINARY_OPERATORS[self.operator](leftValue, rightValue))
