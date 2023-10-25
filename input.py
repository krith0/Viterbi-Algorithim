from PIL import Image

# Open the image file
image = Image.open("spider_man.png")  # Replace "spider_man.png" with your image file name

# Convert the image to grayscale
gray_image = image.convert("L")

# Get the binary pixel data as a list of '0' and '1' strings
binary_data = []
width, height = gray_image.size
threshold = 200  # Set the threshold level

for y in range(height):
    for x in range(width):
        pixel_value = gray_image.getpixel((x, y))
        binary_data.append('1' if pixel_value >= threshold else '0')

# Convert the binary data list to a string
binary_string = ''.join(binary_data)

# Save the binary data as a text file
with open("input_bits.txt", "w") as text_file:
    text_file.write(binary_string)
