import random, math, operator


class ExpressionTree:
    UNARY_OPERATORS = {
        "sin" : math.sin,
        "cos" : math.cos,
        "tan" : math.tan,
        "exp" : math.exp,
        "log" : math.log,
    }
    
    BINARY_OPERATORS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "^": operator.pow,
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
        if random.randint(0,3) == 0:
            self.value = "x"
        else:
            self.value = random.randint(0,10)

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
        self.child = self.generate_child(depth)

    def __str__(self):
        return self.operator + "(" + str(self.child) + ")"
    
    def generate_child(self, depth):
        if depth <= 0:
            return ValueNode()
        
        match random.randint(0,2):
            case 0:
                return ValueNode()
            case 1:
                return UnaryNode(depth - 1)
            case 2:
                return BinaryNode(depth - 1)
            
    def evaluate(self, x):
        value = self.child.evaluate(x)
        return float(ExpressionTree.UNARY_OPERATORS[self.operator](value))
            
            


class BinaryNode():
    def __init__(self, depth):
        self.operator = random.choice(list(ExpressionTree.BINARY_OPERATORS.keys()))
        self.left = self.generate_child(depth)
        self.right = self.generate_child(depth)
    
    def __str__(self):
        return "(" + str(self.left) + " " + self.operator + " " + str(self.right) + ")"

    def generate_child(self, depth):
        if depth <= 0:
            return ValueNode()
        
        match random.randint(0,2):
            case 0:
                return ValueNode()
            case 1:
                return UnaryNode(depth - 1)
            case 2:
                return BinaryNode(depth - 1)
            
    def evaluate(self, x):
        leftValue = self.left.evaluate(x)
        rightValue = self.right.evaluate(x)

        return float(ExpressionTree.BINARY_OPERATORS[self.operator](leftValue, rightValue))

        
tree1 = ExpressionTree(2)
print(str(tree1))
print(tree1.evaluate(1))
