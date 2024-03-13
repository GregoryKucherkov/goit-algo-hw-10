import random


# The function
def f(x):
    return x**2
    
# Checking if points are inside the targeted area
def is_inside(a, b, x, y):
    return y <= f(x) 
    

# Monte Carlo simulation
def monte_carlo_simulation(a, b, num_experiments):
    average_area = 0

    for _ in range(num_experiments):
        
         # Generating random points
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15_000)]

        #  filters a list of points inside targeted area
        inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

        # Calculating the area under the curve by Monte Carlo method
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (a * b)

        average_area += area
    
    # Calculting the average area
    average_area /= num_experiments
    return average_area


# The size of rectangle
a = 2  # the width
b = 4  # the height

num_experiments = 100

# Execution
average_area = monte_carlo_simulation(a, b, num_experiments)
print(f"The average area for {num_experiments} experiments is:{average_area}")

