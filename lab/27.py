def line_equation(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return "The points are identical; no unique line can be determined."
    elif y1 == y2:
        return f"The line is horizontal with equation y = {y1}"
    elif x1 == x2:
        return f"The line is vertical with equation x = {x1}"
    else:
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
        return f"The equation of the line is y = {slope}x + {intercept}"

points = [float(coord) for coord in input("Enter the coordinates of two points (x1 y1 x2 y2): ").split()]

if len(points) != 4:
    print("Please enter exactly four coordinates.")
else:
    x1, y1, x2, y2 = points
    equation = line_equation(x1, y1, x2, y2)
    print(equation)