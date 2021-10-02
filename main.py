# Using K Means to Extract the Dominant Colours from an Image
# https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036
from kmeans import kmeans
from input import user_input_integer, user_input_filename
from PIL import Image
from colormap import rgb2hex
    
# Main
k = user_input_integer("Please enter a K value ", 0, 20)
img_filename = user_input_filename("\nPlease enter the filename to extract the colour palette from (ex. image.jpg)")
img = Image.open(img_filename)
rbg_im = img.convert('RGB')
width, height = img.size

# Loads the RGB values for each pixel in the image into the colours list as a tuple within a list
colours_list = []
for x in range(0, width):
    for y in range(0, height):
        r,g,b = rbg_im.getpixel((x, y))
        new_list = [(r,g,b)]
        colours_list.append(new_list)

print("\nStarting colour palette generation using K-Means")
colour_palette = kmeans(k, colours_list)

# Output hexidecimal colour codes for each colour in generated palette
print("\nColours codes (hex) in your colour palette: ")
for colour in colour_palette:
    print(rgb2hex(colour[0][0],colour[0][1],colour[0][2]))

palette_image = Image.fromarray(colour_palette)
palette_image_path = "./output/colour-palette.png"
palette_image.save(palette_image_path)
print("\nOutput image saved: %s" % palette_image_path)