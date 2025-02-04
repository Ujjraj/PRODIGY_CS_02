from PIL import Image

def encrypt_image(image_path, key):
    # Remove extra quotes from the file path
    image_path = image_path.strip('"')
    
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Encrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))  # Get RGB values of the pixel
            # Perform XOR operation with the key
            r = r ^ key
            g = g ^ key
            b = b ^ key
            img.putpixel((x, y), (r, g, b))  # Update the pixel with encrypted values

    # Save the encrypted image
    encrypted_path = "encrypted_image.png"
    img.save(encrypted_path)
    print(f"Image encrypted and saved as {encrypted_path}")

def decrypt_image(image_path, key):
    # Remove extra quotes from the file path
    image_path = image_path.strip('"')
    
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Decrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))  # Get RGB values of the pixel
            # Perform XOR operation with the key (same as encryption)
            r = r ^ key
            g = g ^ key
            b = b ^ key
            img.putpixel((x, y), (r, g, b))  # Update the pixel with decrypted values

    # Save the decrypted image
    decrypted_path = "decrypted_image.png"
    img.save(decrypted_path)
    print(f"Image decrypted and saved as {decrypted_path}")

def main():
    print("Simple Image Encryption Tool")
    print("----------------------------")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        image_path = input("Enter the path of the image to encrypt: ")
        key = int(input("Enter an encryption key (integer between 0 and 255): "))
        encrypt_image(image_path, key)
    elif choice == "2":
        image_path = input("Enter the path of the encrypted image: ")
        key = int(input("Enter the decryption key (same as encryption key): "))
        decrypt_image(image_path, key)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()