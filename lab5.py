from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image_path):
    """
    Calculate and display the histogram of an image.

    Args:
        image_path (str): Path to the image file.
    """
    # Open the image and convert it to grayscale
    image = Image.open(image_path).convert("L")
    image_data = np.array(image)

    # Calculate the histogram
    histogram, bins = np.histogram(image_data.flatten(), bins=256, range=[0, 256])

    # Normalize the histogram
    histogram = histogram / histogram.sum()

    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.bar(range(256), histogram, color='gray', width=1.0, align='center')
    plt.title("Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Example usage
image_path = "/Users/anastasiaintyakova/Library/Mobile Documents/com~apple~CloudDocs/proga/abl_lab5/37ac8c9bb49edb6c51699591f8a3119b.jpg"  # Replace with your image file path
calculate_histogram(image_path)
