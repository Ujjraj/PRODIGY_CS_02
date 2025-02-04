# PIXEL MANIPULATION FOR IMAGE ENCRYPTION

## DESCRIPTION

The Image Encryption and Decryption Tool is a Python-based application designed to secure images using pixel-level manipulation. This tool employs a simple yet effective encryption technique to transform images into an unreadable format and restore them to their original state using a cipher key. It is an excellent project for understanding the fundamentals of image processing and encryption.

### REQUIREMENTS
- Python 3.x
- Pillow library (pip install pillow)

### HOW DOES IT WORK?

#### Encryption Process
1. Input: An image file (e.g., PNG, JPEG) and a cipher key (an integer between 0 and 255).
2. Pixel Manipulation:
   - Each pixel in the image is composed of three color channels: Red (R), Green (G), and Blue (B).
   - The program applies a bitwise XOR operation to each channel using the secret key.
3. Output: An encrypted image that appears scrambled and visually unrecognizable.

#### Decryption Process
1. Input: The encrypted image and the same cipher key used for encryption.
2. Pixel Manipulation:
   - The program reapplies the XOR operation to each pixel’s color channels using the secret key.
   - This reverses the encryption process, restoring the original pixel values.
3. Output: The decrypted image, identical to the original.

### EXAMPLE USAGE
#### Encrypting an Image
1. Input:
   - Image path: "C:\Users\YourName\Pictures\image.png"
   - Key: "123"
2. Output: Encrypted image saved as "encrypted_image.png".

#### Decrypting an Image
1. Input:
   - Image path: "encrypted_image.png"
   - Key: "123" (Same key used as cipher key)
2. Output: Decrypted image saved as "decrypted_image.png".
