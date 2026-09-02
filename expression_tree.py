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
    def random(cls, depth):
        root = Node.generate_child(depth)
        return cls(root)


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
            new_node = ValueNode()
            self.parent = new_node
            return new_node
        choice = random.randint(0, 2)

        if choice == 0:
            new_node = ValueNode()
            self.parent = new_node
            return new_node
        elif choice == 1:
            new_node = UnaryNode(depth - 1)
            self.parent = new_node
            return new_node
        else:
            new_node = BinaryNode(depth - 1)
            self.parent = new_node
            return new_node




class ValueNode(Node):
    def __init__(self):
        if random.randint(0,1) == 0:
            self.value = "x"
            self.parent = None
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
        self.child: Node = Node.generate_child(depth)
        self.parent: Node = None


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
        self.left: Node = Node.generate_child(depth)
        self.right: Node = Node.generate_child(depth)
        self.parent: Node = None
    
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



expr1 = Expression.random(3)
print(str(expr1))
expr2 = Expression(expr1.root.left.parent)
print(str(expr2))
#nodes = expr2.offspring(expr2.root)
#for each in nodes:
#    print(each.get_value())
