
import colorsys


def convertToHex(color):
    # Convert color value to RGB
    r, g, b = colorsys.hsv_to_rgb(color / 360, 1, 1)
    
    # Convert RGB to hex code
    hex_code = '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))
    
    return hex_code

def generateHexCode(number):
    # Calculate the hue value based on the given number
    hue = (number / 100) * 240  # Adjust the range of the number to fit between 0 and 240
    
    # Convert hue value to RGB
    r, g, b = colorsys.hsv_to_rgb(hue / 360, 1, 1)
    
    # Convert RGB to hex code
    hex_code = '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))
    
    return hex_code

step = 0
for i in range(0, 20):

    print(f"convert: {convertToHex(step)}")
    step += 10
step = 0
for i in range(0, 20):
    print(f"generate: {generateHexCode(step)}")
    step += 10