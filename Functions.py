import numpy as np
import pygame

def random_points(size_x, size_y, count):
    points = []
    colors = []
    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    create_many((1, 1), (int(size_x / 2 - 1), int(size_y / 2) - 1), count, points, colors, color[0])
    create_many((int(size_x / 2 - 1), 1), (int(size_x - 1), int(size_y / 2 - 1)), count, points, colors, color[1])
    create_many((1, int(size_y / 2 - 1)), (int(size_x / 2 - 1), int(size_y - 1)), count, points, colors, color[2])
    create_many((int(size_x / 2 - 1), int(size_y / 2 - 1)), (int(size_x - 1), int(size_y - 1)), count, points, colors, color[3])
    return (points, colors)


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def create_many(min_point, max_point, count, points, colors, color):
    x = np.random.randint(min_point[0], max_point[0], count)
    y = np.random.randint(min_point[1], max_point[1], count)
    for j in range(count):
        points.append([x[j], y[j]])
        colors.append(color)


def draw(screen, points, colors, r):
    screen.fill('WHITE')
    for i in range(len(points)):
        pygame.draw.circle(screen, colors[i], points[i], r)


def get_optimal_neighbors(points, colors, created_points):
    max = 0
    max_i = 0
    count_neigh = len(created_points)
    for i in range(1, len(points) + 1):
        count = knn(points, colors, created_points, i)
        if count > max:
            max = count
            max_i = i
        if max == count_neigh:
            break
    return max_i


def knn(points, colors, created_points, k):
    created_colors = []
    for i in created_points:
        neighbors = []
        for n in range(k):
            min = 1000
            min_i = 0
            for j in range(len(points)):
                distance = dist(points[i][0], points[i][1], points[j][0], points[j][1])
                if j not in neighbors and distance < min and i != j:
                    min = distance
                    min_i = j
            neighbors.append(min_i)
        klasters = [0,0,0,0]
        for i in neighbors:
            if colors[i] == (255, 0, 0):
                klasters[0] += 1
            elif colors[i] == (0, 255, 0):
                klasters[1] += 1
            elif colors[i] == (0, 0, 255):
                klasters[2] += 1
            elif colors[i] == (255, 255, 0):
                klasters[3] += 1
        max = 0
        max_i = 0
        for o in range(len(klasters)):
            if max < klasters[o]:
                max = klasters[o]
                max_i = o
        if max_i == 0:
            created_colors.append((255, 0, 0))
        elif max_i == 1:
            created_colors.append((0, 255, 0))
        elif max_i == 2:
            created_colors.append((0, 0, 255))
        else:
            created_colors.append((255, 255, 0))
    count = 0
    for h in range(len(created_points)):
        if created_colors[h] == colors[created_points[h]]:
            count += 1
    return count


def knn_optimal(points, colors, k, i):
    neighbors = []
    for n in range(k):
        min = 1000
        min_i = 0
        for j in range(len(points)):
            distance = dist(points[i][0], points[i][1], points[j][0], points[j][1])
            if j not in neighbors and distance < min and i != j:
                min = distance
                min_i = j
        neighbors.append(min_i)
    klasters = [0,0,0,0]
    for i in neighbors:
        if colors[i] == (255, 0, 0):
            klasters[0] += 1
        elif colors[i] == (0, 255, 0):
            klasters[1] += 1
        elif colors[i] == (0, 0, 255):
            klasters[2] += 1
        elif colors[i] == (255, 255, 0):
            klasters[3] += 1
    max = 0
    max_i = 0
    for o in range(len(klasters)):
        if max < klasters[o]:
            max = klasters[o]
            max_i = o
    if max_i == 0:
        return (255, 0, 0)
    elif max_i == 1:
        return (0, 255, 0)
    elif max_i == 2:
        return (0, 0, 255)
    else:
        return (255, 255, 0)