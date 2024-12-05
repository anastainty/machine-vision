import cv2
import numpy as np
from matplotlib import pyplot as plt

# Загрузка изображения
img = cv2.imread("/Users/anastasiaintyakova/Library/Mobile Documents/com~apple~CloudDocs/proga/abl_lab5/37ac8c9bb49edb6c51699591f8a3119b.jpg")

# Преобразование изображения в полутоновое
def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Бинаризация изображения с порогом
def binarize_image(gray_img, threshold=128):
    _, binary_img = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY)
    return binary_img

# Выделение границ на полутоновом изображении с помощью оператора Собеля
def sobel_edge_detection(gray_img):
    sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
    edges = cv2.magnitude(sobel_x, sobel_y)
    return np.uint8(edges)

# Выделение границ на бинарном изображении с помощью алгоритма Канни
def canny_edge_detection(binary_img):
    return cv2.Canny(binary_img, 100, 200)

# Функция для отображения изображений
def show_images(images, titles):
    plt.figure(figsize=(12, 6))
    for i in range(len(images)):
        plt.subplot(2, len(images) // 2 + 1, i + 1)
        plt.imshow(images[i], cmap='gray' if len(images[i].shape) == 2 else None)
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# Основной процесс
gray_img = convert_to_grayscale(img)

# Бинаризация изображения
binary_img = binarize_image(gray_img)

# Выделение границ на полутоновом изображении с помощью Собеля
sobel_edges = sobel_edge_detection(gray_img)

# Выделение границ на бинарном изображении с помощью Канни
canny_edges = canny_edge_detection(binary_img)

# Отображение результатов
show_images([gray_img, binary_img, sobel_edges, canny_edges],
            ["Grayscale Image", "Binary Image", "Sobel Edges", "Canny Edges"])
