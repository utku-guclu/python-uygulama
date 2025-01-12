# https://github.com/utku-guclu/python-uygulama.git

## Minimum Öklid Mesafesinin Hesaplanması

# d = √(x₂-x₁)²+(y₂-y₁)²

"""
1. Create a list called "points"
2. List should contain tuples representing points in 2D space. i.e. (x, y)
3. Create a function called euclidienDistance takes two methods - each representing a point (tuple)
4. Using a loop, calculate the Euclidian distance between each pair of 'points' list. Store these distances in another list called 'distances'
5. Find the minimum distance in the 'distances' list and print. 
"""

# Create list of points
points = [(2, 3), (4, 4), (1, 4), (0, 0), (-1, 10)]

def euclidienDistance(p1: tuple, p2: tuple) -> float:
    """ Calculate Euclidian distance between two points """
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]

    return (x_diff * x_diff + y_diff * y_diff) ** .5 # distance 


# Calculate all distances 
distances = []
min_distance = float('inf')
min_points = None

for i in range(len(points)): 
    for j in range(i + 1, len(points)):
        dist = euclidienDistance(points[i], points[j])
        distances.append(dist)

        # Find minimum distance 
        if dist < min_distance:
            min_distance = dist
            min_points = (points[i], points[j])


# Print the minimum distance
print(f"Minimum distance: {min_distance:.2f}")
print(f"Between points: {min_points}")
