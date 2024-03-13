import pulp 

# Model for max production
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

#creating variables
A = pulp.LpVariable('A', lowBound=0, cat='Integer') #lemonade

B = pulp.LpVariable('B', lowBound=0, cat='Integer') #fruit juice

#Define the target funcion(maximize production)
model += A + B, "Maximize Production"

# Add constraints based on the resources
model += 2 * A + B <= 100     # water constraint
model += A <= 50              # sugar constraint
model += A <= 30              # lemon juice constraint
model += 2 * B <= 40          # fruit puree constraint

# Solve the model
model.solve()

# Print the results
print("Status:", pulp.LpStatus[model.status])
print("Optimal amount of Lemonade:", pulp.value(A))
print("Optimal amount of Fruit Juice:", pulp.value(B))
print("Maximum Total Production:", pulp.value(model.objective))

