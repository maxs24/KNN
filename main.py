import pygame
import Functions

if __name__ == '__main__':
    r = 4
    size = (600, 400)
    count = 15

    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.update()
    ret = Functions.random_points(size[0], size[1], count)
    points = ret[0]
    colors = ret[1]
    created_points = []
    new_points = []
    Functions.draw(screen, points, colors, r)
    pygame.display.update()
    play = True
    optimal = False
    optimal_neigh = 0
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if colors[len(points) - 1] != (0,0,0) and optimal_neigh == 0:
                        points.append([event.pos[0], event.pos[1]])
                        colors.append((0,0,0))
                if event.button == 3:
                    if optimal:
                        new_points.append(len(points))
                        points.append([event.pos[0], event.pos[1]])
                        colors.append(Functions.knn_optimal(points, colors, new_points, optimal_neigh, len(points) - 1))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if colors[len(colors) - 1] == (0, 0, 0):
                        colors[len(colors) - 1] = (255, 0, 0)
                        created_points.append(len(colors) - 1)
                if event.key == pygame.K_2:
                    if colors[len(colors) - 1] == (0, 0, 0):
                        colors[len(colors) - 1] = (0, 255, 0)
                        created_points.append(len(colors) - 1)
                if event.key == pygame.K_3:
                    if colors[len(colors) - 1] == (0, 0, 0):
                        colors[len(colors) - 1] = (0, 0, 255)
                        created_points.append(len(colors) - 1)
                if event.key == pygame.K_4:
                    if colors[len(colors) - 1] == (0, 0, 0):
                        colors[len(colors) - 1] = (255, 255, 0)
                        created_points.append(len(colors) - 1)
                if event.key == pygame.K_r:
                    if len(created_points) != 0 and colors[len(colors) - 1] != (0, 0, 0):
                        optimal = True
                        optimal_neigh = Functions.get_optimal_neighbors(points, colors, created_points)
                        print(optimal_neigh)
            Functions.draw(screen, points, colors, r)
            pygame.display.update()