from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    """Encrypt an image using pixel manipulation."""
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply XOR operation with the key to each pixel
    encrypted_array = img_array ^ key

    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    """Decrypt an image (reverse the encryption process)."""
    encrypt_image(image_path, key, output_path)  # XOR again to reverse encryption
    print(f"Decrypted image saved as {output_path}")