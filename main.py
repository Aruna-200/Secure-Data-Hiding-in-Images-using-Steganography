import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import encode_message
from decryption import decode_message
from PIL import Image, ImageTk


# Initialize the Tkinter window
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("400x500")

# Global variables
selected_image = None
stored_password = None
mode = "encode"  # "encode" or "decode"

# Function to upload an image
def upload_image():
    global selected_image, mode
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        selected_image = file_path
        img = Image.open(file_path)
        img = img.resize((250, 250))  # Resize for preview
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img

        # Change mode based on whether the image is already encoded
        if "encrypted_image" in file_path:
            mode = "decode"
            msg_entry.config(state="disabled")  # Disable message input for decoding
            msg_entry.delete(0, tk.END)
        else:
            mode = "encode"
            msg_entry.config(state="normal")  # Enable message input for encoding

        messagebox.showinfo("Success", "Image uploaded successfully!")

# Function to encode a message into an image
def encode_message_wrapper():
    global selected_image, stored_password
    if not selected_image:
        messagebox.showerror("Error", "Please upload an image first!")
        return
    
    msg = msg_entry.get().strip()
    passcode = pass_entry.get().strip()

    if not msg or not passcode:
        messagebox.showerror("Error", "Both message and passcode are required!")
        return

    result = encode_message(selected_image, msg, passcode)

    if "Error" in result:
        messagebox.showerror("Error", result)
    else:
        stored_password = passcode  # Store the password for decoding
        msg_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END)
        img_label.config(image="")  # Clear image preview
        messagebox.showinfo("Success", f"Message encoded successfully! Saved as {result}")

# Function to decode a message from an image
def decode_message_wrapper():
    global selected_image, stored_password

    if not selected_image:
        messagebox.showerror("Error", "Please upload an encrypted image!")
        return

    entered_pass = pass_entry.get().strip()

    result = decode_message(selected_image, stored_password, entered_pass)

    if "Error" in result:
        messagebox.showerror("Error", result)
    else:
        msg_entry.config(state="normal")
        msg_entry.delete(0, tk.END)
        msg_entry.insert(0, result)
        messagebox.showinfo("Success", "Decryption successful!")

# GUI Layout
tk.Label(root, text="Enter Secret Message:").pack()
msg_entry = tk.Entry(root, width=40)
msg_entry.pack()

tk.Label(root, text="Enter Passcode:").pack()
pass_entry = tk.Entry(root, width=40, show="*")
pass_entry.pack()

# Image preview
img_label = tk.Label(root)
img_label.pack()

# Buttons
upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack()

encode_btn = tk.Button(root, text="Encode Message", command=encode_message_wrapper)
encode_btn.pack()

decode_btn = tk.Button(root, text="Decode Message", command=decode_message_wrapper)
decode_btn.pack()

# Run the Tkinter main loop
root.mainloop()
