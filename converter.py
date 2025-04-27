import os
from PIL import Image

# Paths
input_folder = './assets/images/kaijus'
output_folder = './assets/downscaled_images'

# Downscale factor
scale_factor = 4

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported formats
supported_formats = ('.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp', '.png')

# Loop through files
for filename in os.listdir(input_folder):
    if filename.lower().endswith(supported_formats):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Open and downscale
        with Image.open(input_path) as img:
            new_size = (img.width // scale_factor, img.height // scale_factor)
            img_resized = img.resize(new_size, Image.LANCZOS)  # High-quality downscaling
            img_resized.save(output_path)

        print(f"Downscaled {filename} to {new_size}")

print("All images have been downscaled!")
