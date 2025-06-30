from PIL import Image

# Apne image ka file path yahaan likho
input_path = "photo.jpg"         # Input file (jpg, jpeg, etc.)
output_path = "photo_converted.png"  # Output file (png)

# Image open karo
image = Image.open(input_path)

# Convert and save as PNG
image.save(output_path, "PNG")

print(f"Image saved as PNG: {output_path}")
