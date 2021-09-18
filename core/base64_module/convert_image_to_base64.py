import base64

def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read())

image_path = '/Users/krishna/Desktop/1.png'
binary_string = get_base64(image_path)

print('binary_string -> ', binary_string)