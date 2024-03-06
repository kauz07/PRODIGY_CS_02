from PIL import Image

def encrypt_image(image_path, encryption_key):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size
    
    # Convert image to RGB mode
    rgb_image = image.convert('RGB')
    
    # Encrypt the image by applying encryption operation to each pixel
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = rgb_image.getpixel((x, y))
            # Apply encryption operation (e.g., swapping pixel values)
            r_new = (r + encryption_key) % 256
            g_new = (g + encryption_key) % 256
            b_new = (b + encryption_key) % 256
            encrypted_pixels.append((r_new, g_new, b_new))
    
    # Create a new image with the encrypted pixels
    encrypted_image = Image.new('RGB', (width, height))
    encrypted_image.putdata(encrypted_pixels)
    
    # Save the encrypted image
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path, decryption_key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    width, height = encrypted_image.size
    
    # Convert image to RGB mode
    rgb_encrypted_image = encrypted_image.convert('RGB')
    
    # Decrypt the image by applying decryption operation to each pixel
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = rgb_encrypted_image.getpixel((x, y))
            # Apply decryption operation (e.g., undoing the encryption operation)
            r_original = (r - decryption_key) % 256
            g_original = (g - decryption_key) % 256
            b_original = (b - decryption_key) % 256
            decrypted_pixels.append((r_original, g_original, b_original))
    
    # Create a new image with the decrypted pixels
    decrypted_image = Image.new('RGB', (width, height))
    decrypted_image.putdata(decrypted_pixels)
    
    # Save the decrypted image
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    image_path = input("Enter the path to the image you want to encrypt: ")
    encryption_key = int(input("Enter the encryption key: "))
    encrypt_image(image_path, encryption_key)
    
    encrypted_image_path = "encrypted_image.png"
    decryption_key = int(input("Enter the decryption key: "))
    decrypt_image(encrypted_image_path, decryption_key)

if __name__ == "__main__":
    main()
