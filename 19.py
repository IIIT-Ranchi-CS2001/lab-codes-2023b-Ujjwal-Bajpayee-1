import math


point1 = (1, 2, 3)
point2 = (4, 5, 6)


distance = math.sqrt((point1[0] - point2[0]) ** 2 + 
                     (point1[1] - point2[1]) ** 2 + 
                     (point1[2] - point2[2]) ** 2)

print(f"The Euclidean distance between {point1} and {point2} is {distance}")