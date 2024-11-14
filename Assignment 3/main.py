from PIL import Image

def create_collage(images, output_format):
    try:
        images = [Image.open(img) for img in images]
    except Exception as e:
        print(f"Error: Could not open images. {str(e)}")
        return
    
    min_width = min(img.width for img in images)
    min_height = min(img.height for img in images)
    
    images = [img.resize((min_width, min_height)) for img in images]
    
    collage_width = min_width * 2
    collage_height = min_height * 2
    collage = Image.new('RGB', (collage_width, collage_height))

    collage.paste(images[0], (0, 0))
    collage.paste(images[1], (min_width, 0))
    collage.paste(images[2], (0, min_height))
    collage.paste(images[3], (min_width, min_height))

    collage.save(f"collage.{output_format}", format=output_format.upper())
    print(f"Collage created and saved as 'collage.{output_format}'")

images = []
for i in range(1, 5):
    image_path = input(f"Please enter the path for Image {i}: ")
    images.append(image_path)

output_format = input("Please specify the output file format (jpg, png): ")
create_collage(images, output_format)
