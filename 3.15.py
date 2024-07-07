from pulp import *

model = LpProblem("AssemblyProblem", LpMaximize)

# declare variables

X1 = LpVariable("number of acres of wheat planted", 0, None, LpContinuous)
X2 = LpVariable("number of acres of corn planted", 0, None, LpContinuous)
X3 = LpVariable("number of acres of oats planted", 0, None, LpContinuous)
X4 = LpVariable("number of acres of soybeans planted", 0, None, LpContinuous)

model += 622*X1 + 690*X2 + 231*X3 + 684*X4

model += 4*X1 + 5*X2 + 3*X3 + 10*X4 <= 1800, "Labor hours"
model += 50*X1 + 75*X2 + 30*X3 + 60*X4 <= 25000, "Expenses"
model += 2*X1 + 6*X2 + X3 + 4*X4 <= 1200, "Water"
model += 210*X1 >= 30000, "Min. Wheat"
model += 300*X2 >= 30000, "Min. Corn"
model += 180*X3 <= 25000, "Max Oats"
model += X1 + X2 + X3 + X4 <= 300, "Total acres"

# The problem is solved using PuLP's choice of Solver
model.solve()

# Each of the variables is printed with it's resolved optimum value
for v in model.variables():
    print(v.name, "=", v.varValue)