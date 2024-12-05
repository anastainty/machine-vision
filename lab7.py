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

# Устранение шума с помощью усредняющего фильтра
def apply_averaging_filter(img, kernel_size=3):
    return cv2.blur(img, (kernel_size, kernel_size))

# Устранение шума с помощью медианного фильтра
def apply_median_filter(img, kernel_size=3):
    return cv2.medianBlur(img, kernel_size)

# Выделение границ объектов (Собель)
def edge_detection(img):
    edges = cv2.Canny(img, 100, 200)
    return edges

# Функция для отображения изображений
def show_images(images, titles):
    # Устанавливаем размер графика
    plt.figure(figsize=(15, 8))

    # Проходим по всем изображениям
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

# Устранение шума (усредняющий фильтр)
average_filtered_img = apply_averaging_filter(gray_img)

# Устранение шума (медианный фильтр)
median_filtered_img = apply_median_filter(gray_img)

# Выделение границ на бинарном изображении
binary_edges = edge_detection(binary_img)

# Выделение границ на полутоновом изображении
gray_edges = edge_detection(gray_img)

# Отображение результатов
show_images([gray_img, binary_img, average_filtered_img, median_filtered_img, binary_edges, gray_edges],
            ["Grayscale", "Binary", "Averaging Filter", "Median Filter", "Binary Edges", "Gray Edges"])
