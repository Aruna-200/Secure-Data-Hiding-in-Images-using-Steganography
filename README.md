
# Secure Data Hiding in Images using Steganography

## Project Description
This project implements **image-based steganography**, allowing users to **hide secret messages or data inside images** securely. It uses **LSB (Least Significant Bit) encoding** to embed hidden content without noticeable changes to the image.

## Features
- Hide and extract text/messages in images.
- Uses LSB technique for secure data hiding.
- Supports multiple image formats.
- Simple Tkinter GUI for user interaction.

## Technologies Used
- Python
- Tkinter (for GUI)
- Pillow (for image processing)
- NumPy & OpenCV (for advanced image handling)

## Output Workflow
**1️. Upload an Image**
User selects an image to hide a secret message.
The application loads and displays the image.
**2. Enter Secret Message**
User types the message that needs to be hidden inside the image.
The application encodes the message using LSB steganography.
**3️. Hide the Message**
The encoded image is generated with the hidden message.
The modified image looks visually the same as the original.
**4️. Save the Encoded Image**
The user can save the new steganographic image.
The image now contains the hidden message.
**5️. Decode the Message**
User loads the encoded image into the app.
The app extracts and displays the hidden message.


## Installation
Clone the repository and install dependencies:
```sh
git clone https://github.com/Aruna-200/Secure-Data-Hiding-in-Images-using-Steganography
cd SteganographyApp
pip install -r requirements.txt
