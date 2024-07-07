from pulp import *

model = LpProblem("ItemsProblem", LpMaximize)

X1 = LpVariable("$ invested in first trust deeds", 0, None, LpContinuous)
X2 = LpVariable("$ invested in second trust deeds", 0, None, LpContinuous)
X3 = LpVariable("$ invested in third trust deeds", 0, None, LpContinuous)
X4 = LpVariable("$ invested in commercial trust deeds", 0, None, LpContinuous)
X5 = LpVariable("$ invested in a savings account", 0, None, LpContinuous)
X6 = LpVariable("Total $ invested in residential trust deeds", 0, None, LpContinuous)
X7 = LpVariable("Total $ invested in all trust deeds", 0, None, LpContinuous)

model += .0775*X1 + 0.1125*X2 + .1425*X3 + .9875*X4 + .0445*X5

model += X1 + X2 + X3 + X4 + X5 == 68000000, "Total"
model += X5 >= 5000000, "Save"
model += X1 + X2 + X3 + - X6 == 0,"Res Tr."
model += X1 + X2 + X3 + X4 - 1*X7 == 0, "Total Tr"
model += X6 - .8*X7 >= 0, "80% Res."
model += X1 - .6*X6 >= 0, "60% First"
model += 4*X1 + 6*X2 + 9*X3 + 3*X4 <= 340000000, "average Risk factor"


# The problem is solved using PuLP's choice of Solver
model.solve()

# Each of the variables is printed with it's resolved optimum value
for v in model.variables():
    print(v.name, "=", v.varValue)