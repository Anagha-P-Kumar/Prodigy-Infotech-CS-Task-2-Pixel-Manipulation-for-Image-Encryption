# Task2-Pixel-Manipulation-for-Image-Encryption
Pixel manipulation for image encryption involves modifying the pixel values of an image to make it unreadable or protected from unauthorized access. This method ensures confidentiality by altering the Red, Green, and Blue (RGB) values of each pixel using various cryptographic or mathematical techniques.

# Concept of Pixel Manipulation
Each image is represented as a matrix of pixels, where each pixel has three color components (RGB) in an 8-bit range (0-255). By applying transformations like XOR operations, bitwise shifts, or mathematical functions, we can encrypt and decrypt an image.

# Steps for Image Encryption
- Read the Image: Convert the image into a NumPy array.
- Apply Encryption Algorithm: Modify pixel values using a key.
- Save the Encrypted Image: Store the modified pixel values.
- Decryption: Reverse the transformation using the same key.

# Image Encryption Tool

This script provides a simple image encryption and decryption tool using pixel shuffling.

## Features
- Encrypts an image by shuffling its pixel positions using a key.
- Decrypts the encrypted image back to its original form when the correct key is used.
- Uses a simple key-based approach for encryption security.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Usage
1. Place an image named `input.jpg` in the same directory as the script.
2. Run the script using `python script.py`.
3. The encrypted image will be saved as `encrypted.jpg`.
4. The decrypted image will be saved as `decrypted.jpg`.
