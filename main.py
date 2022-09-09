from PIL import Image, ImageEnhance
from datetime import datetime
import sys

#valid_image_formats = [
#    ".png",
#    ".jpg",
#    ".jpeg",
#    ]

def resize_image(img, width, height):
    resized_image = img.resize((width, height))
    resized_image.show()
    resized_image.save(f"resize_images/img_{str(datetime.now().date())}.jpg")


def enhance_image(img, factor):
    img_copy = img.copy()
    sharpness = ImageEnhance.Sharpness(img_copy)
    sharpness.enhance(factor)
    img_copy.show()
    img_copy.save(f"enhanced_images/img_{str(datetime.now().date())}.jpg")
    

def main():
    valid_option = False
    option = None
    while not valid_option:
        option = input("Press 1 for image resize option\nPress 2 for Image enhancement option\n Select Options: ")
        if option == "1":
            valid_dimension = False
            while not valid_dimension:
                dimension = input("Enter the new width and height separated by comma, (width,height): ")
                if len(dimension.split(",")) != 2:
                    print("Dimension must be in the format width,height")
                    continue 
                else:
                    width, height = dimension.split(",")
                    width, height = width.strip(), height.strip()
                    valid_dimension = True
            break
        elif option == "2":
            factor = float(input("Enter the enhancement factor, example 1.5: "))
            break
        else:
            print("Invalid Option try again... options are 1 and 2")

    image_file = input(r"Enter the Path to Image File: ")
    try:
        img = Image.open(image_file)
    except Exception as err:
        print(err)
        print(f"Can not open the file: \"{image_file}\", start again")
        return
    
    match option:
        case "1":
            resize_image(img, int(width), int(height))
        case "2":
            enhance_image(img, factor)

    start_again = input("To restart press s: ")
    if start_again.lower() == "s":
        return main()
    
if __name__ == "__main__":
    main()
