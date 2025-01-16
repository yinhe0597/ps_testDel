from PIL import Image
import os

def remove_adobe_metadata(image_path):
    """Remove Adobe metadata from an image file"""
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Remove all metadata
        data = list(img.getdata())
        clean_img = Image.new(img.mode, img.size)
        clean_img.putdata(data)
        
        # Create ycl folder if not exists
        output_dir = os.path.join(os.path.dirname(image_path), "ycl")
        os.makedirs(output_dir, exist_ok=True)
        
        # Save the cleaned image
        filename = os.path.basename(image_path)
        output_path = os.path.join(output_dir, filename)
        clean_img.save(output_path, quality=95)
        
        print(f"Processed: {image_path} -> {output_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")
        return False

def batch_process_images(folder_path):
    """Process all images in a folder"""
    supported_formats = ['.jpg', '.jpeg', '.png', '.tiff']
    
    for filename in os.listdir(folder_path):
        if any(filename.lower().endswith(ext) for ext in supported_formats):
            full_path = os.path.join(folder_path, filename)
            remove_adobe_metadata(full_path)

if __name__ == "__main__":
    # Example usage
    image_folder = "images"  # Folder containing images to process
    if os.path.exists(image_folder):
        batch_process_images(image_folder)
    else:
        print(f"Folder '{image_folder}' not found. Please create it and place your images there.")
