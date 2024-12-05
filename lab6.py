from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def convert_to_grayscale(image_path):
    # Открываем изображение
    image = Image.open(image_path)

    # Преобразуем изображение в оттенки серого
    grayscale_image = image.convert("L")

    # Сохраняем или отображаем изображение
    grayscale_image.save('grayscale_image.png')
    grayscale_image.show()

    return grayscale_image


def binarize_image(grayscale_image, threshold=128):
    # Преобразуем изображение в numpy array
    grayscale_array = np.array(grayscale_image)

    # Применяем порог для бинаризации
    binary_array = np.where(grayscale_array >= threshold, 255, 0)

    # Преобразуем обратно в изображение
    binary_image = Image.fromarray(binary_array.astype(np.uint8))

    # Сохраняем или отображаем бинаризованное изображение
    binary_image.save('binary_image.png')
    binary_image.show()

    return binary_image


def plot_histogram(image):
    # Преобразуем изображение в numpy array
    image_array = np.array(image)

    # Строим гистограмму
    plt.hist(image_array.flatten(), bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.title("Histogram of Grayscale Image")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()


# Пример использования

image_path = "/Users/anastasiaintyakova/Library/Mobile Documents/com~apple~CloudDocs/proga/abl_lab5/37ac8c9bb49edb6c51699591f8a3119b.jpg"  # Путь к изображению

# Преобразуем в полутоновое изображение
grayscale_image = convert_to_grayscale(image_path)

# Строим гистограмму
plot_histogram(grayscale_image)

# Бинаризуем изображение с порогом 128
binary_image = binarize_image(grayscale_image, threshold=128)
