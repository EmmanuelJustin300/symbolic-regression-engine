import random, math, operator

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
    return math.pow(a, b)

def generate_random_node(depth):
    if depth <= 0:
        return ValueNode()

    choice = random.randint(0, 2)

    if choice == 0:
        return ValueNode()
    elif choice == 1:
        return UnaryNode(depth - 1)
    else:
        return BinaryNode(depth - 1)


class ExpressionTree:
    UNARY_OPERATORS = {
        "sin" : math.sin,
        "cos" : math.cos,
        "tan" : math.tan,
        "exp" : math.exp,
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




class ValueNode():
    def __init__(self):
        if random.randint(0,1) == 0:
            self.value = "x"
        else:
            if random.random() < 0.7:
                self.value = random.randint(-5, 5)
            else:
                self.value = round(random.uniform(-10, 10), 2)

    def __str__(self):
        return str(self.value)
    
    
    def evaluate(self, x):
        if self.value == "x":
            return float(x)
        else:
            return float(self.value)
        


class UnaryNode():
    def __init__(self, depth):
        self.operator = random.choice(list(ExpressionTree.UNARY_OPERATORS.keys()))
        self.child = generate_random_node(depth)

    def __str__(self):
        return self.operator + "(" + str(self.child) + ")"
    
            
    def evaluate(self, x):
        value = self.child.evaluate(x)
        return float(ExpressionTree.UNARY_OPERATORS[self.operator](value))
            
            

class BinaryNode():
    def __init__(self, depth):
        self.operator = random.choice(list(ExpressionTree.BINARY_OPERATORS.keys()))
        self.left = generate_random_node(depth)
        self.right = generate_random_node(depth)
    
    def __str__(self):
        return "(" + str(self.left) + " " + self.operator + " " + str(self.right) + ")"
    
            
    def evaluate(self, x):
        leftValue = self.left.evaluate(x)
        rightValue = self.right.evaluate(x)

        return float(ExpressionTree.BINARY_OPERATORS[self.operator](leftValue, rightValue))
