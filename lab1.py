import tkinter as tk
from tkinter import colorchooser

def step_by_step_algorithm(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    x = x0
    y = y0
    points = [(round(x), round(y))]

    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))

    return points

def dda_algorithm(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    x = x0
    y = y0
    points = [(round(x), round(y))]

    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))

    return points

def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return points

def bresenham_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    d = 3 - 2 * r
    while y >= x:
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ])
        if d <= 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

def bresenham_ellipse(xc, yc, a, b):
    points = []
    x, y = 0, b
    a2, b2 = a * a, b * b
    two_a2, two_b2 = 2 * a2, 2 * b2

    # Первая часть: от оси X до перехода
    d1 = b2 - (a2 * b) + (0.25 * a2)
    dx, dy = 0, two_a2 * y
    while dx < dy:
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y)
        ])
        if d1 < 0:
            x += 1
            dx += two_b2
            d1 += dx + b2
        else:
            x += 1
            y -= 1
            dx += two_b2
            dy -= two_a2
            d1 += dx - dy + b2

    # Вторая часть: от перехода до оси Y
    d2 = (b2 * ((x + 0.5) ** 2)) + (a2 * ((y - 1) ** 2)) - (a2 * b2)
    while y >= 0:
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y)
        ])
        if d2 > 0:
            y -= 1
            dy -= two_a2
            d2 += a2 - dy
        else:
            y -= 1
            x += 1
            dx += two_b2
            d2 += dx - dy + a2

    return points

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Raster Algorithms Paint")

        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.color = 'black'
        self.algorithm = tk.StringVar(value='step_by_step')
        self.start_x, self.start_y = None, None
        self.create_widgets()
        self.create_grid()

        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def create_widgets(self):
        toolbar = tk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        color_btn = tk.Button(toolbar, text="Color", command=self.choose_color)
        color_btn.pack(side=tk.LEFT)

        algorithm_menu = tk.OptionMenu(toolbar, self.algorithm, "step_by_step", "dda", "bresenham", "bresenham_circle", "bresenham_ellipse")
        algorithm_menu.pack(side=tk.LEFT)

        clear_btn = tk.Button(toolbar, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT)

        self.coord_label = tk.Label(toolbar, text="Coordinates: ")
        self.coord_label.pack(side=tk.RIGHT)

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def clear_canvas(self):
        self.canvas.delete("all")
        self.create_grid()

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_button_release(self, event):
        if self.start_x is not None and self.start_y is not None:
            x1, y1 = event.x, event.y
            if self.algorithm.get() == "bresenham_circle":
                r = int(((x1 - self.start_x) ** 2 + (y1 - self.start_y) ** 2) ** 0.5)
                points = bresenham_circle(self.start_x, self.start_y, r)
            elif self.algorithm.get() == "bresenham_ellipse":
                a = abs(x1 - self.start_x)
                b = abs(y1 - self.start_y)
                points = bresenham_ellipse(self.start_x, self.start_y, a, b)
            else:
                points = self.get_points(self.start_x, self.start_y, x1, y1)

            for x, y in points:
                self.canvas.create_line(x, y, x + 1, y + 1, fill=self.color)

            self.coord_label.config(text=f"Coordinates: ({self.start_x}, {self.start_y}) to ({x1}, {y1})")

        self.start_x = None
        self.start_y = None

    def get_points(self, x0, y0, x1, y1):
        algo = self.algorithm.get()
        if algo == 'step_by_step':
            return step_by_step_algorithm(x0, y0, x1, y1)
        elif algo == 'dda':
            return dda_algorithm(x0, y0, x1, y1)
        elif algo == 'bresenham':
            return bresenham_line(x0, y0, x1, y1)
        elif algo == 'bresenham_circle':
            return []
        elif algo == 'bresenham_ellipse':
            return []

    def create_grid(self):
        for i in range(0, 800, 10):
            self.canvas.create_line([(i, 0), (i, 600)], tag='grid_line', fill='lightgrey')
        for i in range(0, 600, 10):
            self.canvas.create_line([(0, i), (800, i)], tag='grid_line', fill='lightgrey')
        self.canvas.create_line(400, 0, 400, 600, fill='black', width=2)
        self.canvas.create_line(0, 300, 800, 300, fill='black', width=2)
        self.canvas.create_text(410, 10, text="Y", anchor=tk.NW, fill="black")
        self.canvas.create_text(790, 310, text="X", anchor=tk.NE, fill="black")

def main():
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
