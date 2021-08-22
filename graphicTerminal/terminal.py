import pygame

white = (255, 255, 255)
pen_size = 1
pen_color = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((300, 300))
screen.fill(white)
while True:
    pygame.event.pump()
    exp = input().split()
    if exp[0] == "change":
        if exp[1] == "size":
            pen_size = int(exp[2])
        elif exp[1] == "color":
            pen_color = tuple(map(int, (exp[2], exp[3], exp[4])))
    elif exp[0] == "draw":
        if exp[1] == "line":
            first_position = tuple(map(int, (exp[2], exp[3])))
            second_position = tuple(map(int, (exp[4], exp[5])))
            pygame.draw.line(
                screen, pen_color, first_position, second_position, pen_size
            )
        elif exp[1] == "circle":
            center = tuple(map(int, (exp[2], exp[3])))
            radius = int(exp[4])
            pygame.draw.circle(screen, pen_color, center, radius, pen_size)
        elif exp[1] == "polygon":
            edges = list()
            while len(exp[2:]) > 0:
                x = exp.pop(2)
                y = exp.pop(2)
                edges.append((int(x), int(y)))
            pygame.draw.polygon(screen, pen_color, edges, pen_size)
    elif exp[0] == "end" and exp[1] == "drawing":
        break
    pygame.display.update()

pygame.image.save(screen, "draw.png")
