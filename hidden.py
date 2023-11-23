 
import os
import string
from PIL import Image
  
  
def encode_image(img, msg):
    """
    use the red portion of an image (r, g, b) tuple to
    hide the msg string characters as ASCII values
    red value of the first pixel is used for length of string
    """
    length = len(msg)
    # limit length of message to 255
    if length > 255:
        print("text too long! (don't exeed 255 characters)")
        return False
    if img.mode != 'RGB':
        print("image mode needs to be RGB")
        return False
    # use a copy of image to hide the text in
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            # first value is length of msg
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = msg[index -1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g , b))
            index += 1
    return encoded



# pick a .png or .bmp file you have in the working directory
# or give full path name
original_image_file = "Beach7.jpg"
#original_image_file = "Beach7.bmp"

img = Image.open(original_image_file)
# image mode needs to be 'RGB'
print(img, img.mode)  # test

# create a new filename for the modified/encoded image
encoded_image_file = "enc_" + original_image_file

# don't exceed 255 characters in the message
secret_msg = "this is a secret message added to the image"
print(len(secret_msg))  # test

img_encoded = encode_image(img, secret_msg)

if img_encoded:
    # save the image with the hidden text
    img_encoded.save(encoded_image_file)
    print("{} saved!".format(encoded_image_file))

    # view the saved file, works with Windows only
    # behaves like double-clicking on the saved file
    
    os.startfile(encoded_image_file)
    
