from PIL import Image

# Load the image
input_path = "input.jpg"  # Change this to your image path
output_path = "output.png"

# Convert and save
image = Image.open(input_path)
image.save(output_path, "PNG")

print("Image converted to PNG successfully!")
