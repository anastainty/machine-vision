import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Функция для рисования многоугольника
def draw_polygon(ax, polygon, color, label=None, alpha=1.0):
    x, y = polygon.exterior.xy
    ax.fill(x, y, color=color, alpha=alpha, label=label)
    ax.plot(x, y, color="black", linewidth=1)

# Основная функция для отсечения
def clip_polygon(subject_coords, clip_coords):
    subject_polygon = Polygon(subject_coords)
    clip_polygon = Polygon(clip_coords)
    intersection = subject_polygon.intersection(clip_polygon)  # Находим пересечение
    return intersection

# Данные: два многоугольника
subject_polygon_coords = [
    (150, 50),
    (250, 50),
    (300, 150),
    (200, 250),
    (100, 150)
]

clip_polygon_coords = [
    (175, 100),
    (225, 100),
    (225, 200),
    (175, 200)
]

# Основная часть: построение графика
fig, ax = plt.subplots(figsize=(6, 6))

# Исходные многоугольники
subject_polygon = Polygon(subject_polygon_coords)
clip_window = Polygon(clip_polygon_coords)

# Отсечение
result_polygon = clip_polygon(subject_polygon_coords, clip_polygon_coords)

# Рисуем многоугольники
draw_polygon(ax, subject_polygon, color="#FF6400", label="Subject Polygon", alpha=0.5)
draw_polygon(ax, clip_window, color="#990000", label="Clipping Window", alpha=0.5)

# Рисуем результат
if not result_polygon.is_empty:
    draw_polygon(ax, result_polygon, color="#0000FF", label="Clipped Polygon", alpha=0.7)

# Оформляем график
ax.set_xlim(50, 350)
ax.set_ylim(50, 350)
ax.set_aspect('equal', adjustable='box')
ax.legend()
ax.set_title("Отсечение многоугольников")
plt.show()
