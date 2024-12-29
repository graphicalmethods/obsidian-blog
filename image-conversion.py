from PIL import Image, ImageOps
import os

def compress_image(input_path, output_path, quality=85):
    """
    Compresses an image using the specified quality.
    
    :param input_path: Path to the input image file.
    :param output_path: Path to save the compressed image file.
    :param quality: Compression quality (0-100), where 100 is no compression.
    """
    # Open the image
    with Image.open(input_path) as img:
        # Correct the orientation based on EXIF data
        img = ImageOps.exif_transpose(img)
        # Convert image to RGB mode if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        # Save the image with the specified quality
        img.save(output_path, 'WEBP', quality=quality)

def compress_images_in_directory(input_dir, output_dir, quality=80):
    """
    Compresses all JPEG images in a directory.
    
    :param input_dir: Directory containing input images.
    :param output_dir: Directory to save compressed images.
    :param quality: Compression quality (0-100), where 100 is no compression.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(output_dir, name + '.webp')
            try:
                compress_image(input_path, output_path, quality)
                print(f"Compressed {input_path} to {output_path}")
            except Exception as e:
                print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    input_directory = './raw_images/'
    output_directory = './assets/images/'
    compression_quality = 80  # Adjust this value (0-100) for desired compression level

    compress_images_in_directory(input_directory, output_directory, compression_quality)