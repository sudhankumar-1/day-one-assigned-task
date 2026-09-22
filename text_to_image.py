import sys
from PIL import Image, ImageDraw, ImageFont

def text_to_image(text_file, image_file):
    with open(text_file, 'r') as f:
        text = f.read()

    # Create a blank image with black background
    img = Image.new('RGB', (800, 400), color=(0, 0, 0))
    d = ImageDraw.Draw(img)

    # Use a default font
    try:
        font = ImageFont.truetype("consola.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    # Draw the text
    d.text((10, 10), text, fill=(255, 255, 255), font=font)

    # Save the image
    img.save(image_file)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        text_to_image(sys.argv[1], sys.argv[2])
