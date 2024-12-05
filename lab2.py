import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_star():
    # Координаты звезды
    coordinates = [
        (200, 100),
        (230, 160),
        (300, 160),
        (250, 200),
        (270, 260),
        (200, 220),
        (135, 260),
        (150, 200),
        (100, 160),
        (170, 160)
    ]

    # Создаём фигуру и оси
    fig, ax = plt.subplots()

    # Создаём многоугольник и закрашиваем
    star = patches.Polygon(coordinates, closed=True, facecolor='#FF6400', edgecolor='black')
    ax.add_patch(star)

    # Настраиваем отображение
    ax.set_xlim(50, 350)
    ax.set_ylim(50, 300)
    ax.set_aspect('equal', adjustable='box')
    plt.title("Закрашивание звезды")
    plt.show()

# Вызываем функцию
draw_star()
