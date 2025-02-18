import cv2

def decode_message(image_path, stored_password, entered_pass):
    if stored_password is None:
        return "No stored password found. Encode an image first!"

    if entered_pass != stored_password:
        return "Incorrect passcode!"

    img = cv2.imread(image_path)

    if img is None:
        return "Error loading image!"

    message = ""
    n, m, z = 0, 0, 0
    height, width, _ = img.shape

    while n < height:
        char = chr(img[n, m, z])  # Extract character from pixel
        if message.endswith("ENDMSG"):
            message = message[:-6]  # Remove the marker
            break
        message += char
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == width:
                m = 0
                n += 1

    return message
