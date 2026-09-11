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
        return random.choice(self.get_nodes(self.root))


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

    def get_nodes(self, node):
        nodes = [node]

        for child in node.get_children():
            nodes.extend(self.get_nodes(child))

        return nodes

    def replace_node(self, old_node, new_node):
        if old_node is self.root:
            self.root = new_node
            return True
        
        parent = self.find_parent(old_node)

        if parent is None:
            raise ValueError(f"Node not found in expression: {old_node}")

        parent.replace_child(old_node, new_node)
        return True


    def find_parent(self, target_node):
        for each in self.get_nodes(self.root):
            if target_node in each.get_children():
                return each




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

    def replace_child(self, old_child, new_child):
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
            return Node.generate_terminal()
        
        choice = random.randint(0, 2)
        if choice == 0:
            return Node.generate_terminal()
        elif choice == 1:
            operator = random.choice(list(Expression.UNARY_OPERATORS.keys()))
            child = Node.generate_child(depth - 1)
            return UnaryNode(operator, child)
        else:
            operator = random.choice(list(Expression.BINARY_OPERATORS.keys()))
            left = Node.generate_child(depth - 1)
            right = Node.generate_child(depth - 1)
            return BinaryNode(operator, left, right)


    @staticmethod
    def generate_terminal():
        if random.choice([True, False]):
            return VariableNode("x")

        if random.random() < 0.7:
            value = random.randint(-5, 5)
        else:
            value = round(random.uniform(-100, 100), 2)

        return ConstantNode(value)




class VariableNode(Node):
    def __init__(self, variable):
        self.value = str(variable)

    def __str__(self):
        return self.value

    def get_value(self):
        return str(self)
    
    
    def evaluate(self, x):
        return float(x)


    def get_children(self):
        return []

    def replace_child(self, old_child, new_child):
        return


class ConstantNode(Node):
    def __init__(self, value):
        self.value = float(value)


    def __str__(self):
        return str(self.value)

    def get_value(self):
        return str(self)
    
    
    def evaluate(self, x=None):
        return float(self.value)


    def get_children(self):
        return []
        
    def replace_child(self, old_child, new_child):
        return

class UnaryNode(Node):
    def __init__(self, operator, child):
        if operator not in Expression.UNARY_OPERATORS:
            raise ValueError(f"Invalid unary operator: {operator}")

        self.operator = operator
        self.child = child


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

    def replace_child(self, old_child, new_child):
        if self.child is old_child:
            self.child = new_child
            return True
        return False
            
            

class BinaryNode(Node):
    def __init__(self, operator, left, right):
        if operator not in Expression.BINARY_OPERATORS:
            raise ValueError(f"Invalid binary operator: {operator}")

        self.operator = operator
        self.left = left
        self.right = right

    
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

    def replace_child(self, old_child, new_child):
        if self.left is old_child:
            self.left = new_child
            return True
        elif self.right is old_child:
            self.right = new_child
            return True
        return False


expr = Expression(
    BinaryNode(
        "+",
        VariableNode("x"),
        ConstantNode(5)
        )
)

print(expr)

expr.replace_node(expr.root.left, ConstantNode(2))
print(expr)

expr.replace_node(expr.root, VariableNode("x"))
print(expr)