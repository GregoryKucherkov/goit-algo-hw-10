from scipy import integrate

# Limits
a = 0
b = 2

def f(x):
    return x**2

result, error = integrate.quad(f, a, b)

print(f"The result of numerical integration: {result}")
print(f"Estimated error: {error}")

