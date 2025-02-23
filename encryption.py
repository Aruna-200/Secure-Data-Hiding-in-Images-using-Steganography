import cv2
import os

def encode_message(image_path, msg, passcode):
    msg += "ENDMSG"  # Unique marker to detect end of message
    img = cv2.imread(image_path)

    if img is None:
        return "Error loading image!"

    height, width, _ = img.shape
    max_chars = height * width * 3  # Maximum message length

    if len(msg) > max_chars:
        return f"Message too long! Max: {max_chars} characters."

    # Encode message into the image pixels
    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = ord(char)  # Convert character to ASCII value and store in pixel
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == width:
                m = 0
                n += 1
                if n == height:
                    break  

    # Save the encoded image
    encrypted_image_path = os.path.join(os.getcwd(), "encrypted_image.png")
    cv2.imwrite(encrypted_image_path, img)

    return encrypted_image_path
