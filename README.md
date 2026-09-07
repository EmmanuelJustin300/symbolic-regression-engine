# Symbolic Regression Engine

A symbolic regression engine using Python to search for mathematical expressions to fit a set of data points.

The project represents mathematical expressions as recursive syntax trees and is being developed into a genetic programming system capable of evolving increasingly accurate candidate expressions over multiple generations.

## Current Features

* Random mathematical expression generation
* Tree-based expression representation
* Recursive expression evaluation
* Unary operators:

  * `sin`
  * `cos`
  * `tan`
  * `exp`
  * `log`
* Binary operators:

  * `+`
  * `-`
  * `*`
  * `/`
  * `^`
* Protected mathematical operations for invalid domains and overflow
* Random dataset generation from generated expressions
* Population generation
* Mean Squared Error (MSE) fitness evaluation
* Candidate ranking by fitness
* Recursive tree traversal for accessing individual expression nodes

## How It Works

Each candidate solution is represented as an expression tree.

For example:

```text
(x + sin(x))
```

can be represented conceptually as:

```text
        +
       / \
      x  sin
          |
          x
```

The engine can recursively evaluate these trees for different values of `x`.

A population of randomly generated expressions can then be evaluated against a set of training points using Mean Squared Error:

```text
Population
    ↓
Evaluate expressions
    ↓
Calculate MSE
    ↓
Rank candidate expressions
```

The next stage of development will extend this process into a complete genetic programming loop.

## Example

A random expression can be created using:

```python
from expression_tree import Expression

expression = Expression.random(4)

print(expression)
print(expression.evaluate(2))
```

An existing expression tree can also be wrapped directly:

```python
expression = Expression(existing_root)
```

This separation allows expressions produced through mutation or crossover to be reused without generating an entirely new random tree.

## Dataset Generation

The project can generate synthetic datasets from randomly generated expressions.

For example, an expression such as:

```text
((x * 3) + sin(x))
```

can be evaluated at randomly selected values of `x` to produce training points:

```text
x, y
-2.0, -6.909
-1.0, -3.841
 0.0,  0.000
 1.0,  3.841
 2.0,  6.909
```

These datasets can then be used to test whether the symbolic regression engine can rediscover an expression that approximates the original function.

## Fitness Evaluation

Candidate expressions are scored using Mean Squared Error:

```text
MSE = average of (actual_y - predicted_y)^2
```

Lower scores represent better candidate expressions.

Expressions which produce invalid numerical values are rejected during fitness evaluation.

## Project Structure

```text
symbolic-regression-engine/
│
├── expression_tree.py
│   ├── Expression
│   ├── Node
│   ├── ValueNode
│   ├── UnaryNode
│   └── BinaryNode
│
├── gen.py
│   └── Synthetic dataset generation
│
├── best_fit.py
│   ├── Population generation
│   ├── Fitness evaluation
│   └── Candidate ranking
│
└── Data/
    └── Generated datasets
```

## Planned Features

The next stages of development are:

* Constant mutation
* Operator mutation
* Subtree mutation
* Genetic crossover
* Parent selection
* Elitism
* Multi-generation evolution
* Expression depth and complexity constraints
* Complexity penalties to reduce tree bloat
* Automated testing
* Improved result visualisation
* Full command-line or web interface

The intended evolution process is:

```text
Initial Population
       ↓
Fitness Evaluation
       ↓
Parent Selection
       ↓
Crossover
       ↓
Mutation
       ↓
New Population
       ↓
Repeat
```

## Goal

The long-term goal is to create a complete symbolic regression system capable of discovering compact mathematical relationships from numerical data using genetic programming rather than predefined regression models.

The project is being built from scratch to explore:

* Genetic programming
* Tree data structures
* Recursive algorithms
* Evolutionary optimisation
* Numerical error handling
* Object-oriented design
* Algorithm performance and optimisation
