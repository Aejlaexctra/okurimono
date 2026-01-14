import numpy as np
from PIL import Image

# Get image
img = Image.open("frames/6.png")
arr = np.array(img) 
arr = arr.reshape((64,3))

def clamp(x): 
  return max(0, min(x, 255))

# Make hexadecimal string
rgb_hex_str = ""
for i in range(64):
    RGB = arr[i,:]
    R = RGB[0]
    G = RGB[1]
    B = RGB[2]
    rgb_hex = "{0:02x}{1:02x}{2:02x}".format(clamp(R), clamp(G), clamp(B)).upper()
    rgb_hex = "0x" + rgb_hex
    rgb_hex_str += rgb_hex

print(rgb_hex_str)
    