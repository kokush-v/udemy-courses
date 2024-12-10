from PIL import Image
import numpy as np
from collections import Counter


def get_top_colors(image_path, top_n=20):
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)

    pixels = image_array.reshape(-1, image_array.shape[-1])
    pixel_list = [tuple(pixel) for pixel in pixels]

    color_counts = Counter(pixel_list)
    top_colors = color_counts.most_common(top_n)
    top_colors_hex = [(f"#{r:02x}{g:02x}{b:02x}", (count/len(pixel_list))*100)
                      for ((r, g, b), count) in top_colors]

    return top_colors_hex


image_path = "example.jpg"
top_colors = get_top_colors(image_path, top_n=10)

for color, count in top_colors:
    print(f"Color: {color}, Percentage: {count}")
