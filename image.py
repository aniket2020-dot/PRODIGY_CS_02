from PIL import Image

def encrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print(f"Decrypted image saved as {output_path}")

encrypt_image("input.jpg", "encrypted.png", key=50)
decrypt_image("encrypted.png", "decrypted.png", key=50)
