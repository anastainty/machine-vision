import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np

# Данные исходных точек
graphic_points = [
    (0, 200),
    (50, 300),
    (100, 100),
    (150, 170),
    (200, 120),
    (250, 250),
    (300, 300),
    (350, 50),
    (400, 100),
    (450, 200),
    (500, 150),
    (550, 300),
    (600, 120),
    (650, 200),
    (700, 230),
    (750, 200)
]

# Разделяем координаты
x_points, y_points = zip(*graphic_points)

# Построение графика
fig, ax = plt.subplots(figsize=(10, 5))

# Рисуем координатные оси
ax.axhline(200, color='black', linewidth=1, linestyle='--')
ax.axvline(0, color='black', linewidth=1, linestyle='--')
ax.set_xlim(0, 800)
ax.set_ylim(0, 400)

# Рисуем исходные точки
ax.scatter(x_points, y_points, color='blue', label='Точки', zorder=5)

# Рисуем ломаную линию
ax.plot(x_points, y_points, color='green', linestyle='--', label='Ломаная', linewidth=1.5)

# Аппроксимация с использованием сплайна (гладкой кривой)
spline = CubicSpline(x_points, y_points)
x_new = np.linspace(min(x_points), max(x_points), 500)
y_new = spline(x_new)

# Рисуем сплайн
ax.plot(x_new, y_new, color='red', label='Аппроксимация (Cubic Spline)', linewidth=2)

# Настройки графика
ax.set_title('Аппроксимация кривой и ломаная линия')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
ax.grid(True)
plt.show()
