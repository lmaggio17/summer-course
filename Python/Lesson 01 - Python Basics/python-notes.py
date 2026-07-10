def pythagorean_theorem(a, b):
    c_squared = a**2 + b**2
    c = c_squared ** 0.5
    return c


a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

c = pythagorean_theorem(a, b)
print(f"For a = {a} and b = {b}, c = {c:.2f}")
