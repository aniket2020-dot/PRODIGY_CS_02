from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()

    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, key)

if _name_ == "_main_":
    print("=== Image Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().lower()
    input_file = input("Enter input image file name (with extension): ").strip()
    output_file = input("Enter output image file name (with extension): ").strip()
    key = int(input("Enter numeric key (0-255): ").strip())

    if choice == 'e':
        encrypt_image(input_file, output_file, key)
    elif choice == 'd':
        decrypt_image(input_file, output_file, key)
    else:
        print("Invalid choice!")
