from pathlib import Path
from PIL import Image, ImageDraw

def imageprocess(image_path, output_path = 'output'):
    """Prepare image to be suitable for MachineLearning

    Takes image at filepath and crops the vendor info bar off 
    the bottom. It also blocks out the vendor logo in the lower
    left corner.
    
    Example:
    >>> imageprocess("/path/to/image.jpg", "/path/to/output/")

    Keyword arguments:
    image_path  -- the path to the image
    output_path -- the path the modified image is saved to. Defaults to output
    """

    # Check we have an output path, otherwise the code would
    # overwrite the original!
    if not output_path:
        raise ValueError("An output path must be provided.")
        
    im = Image.open(image_path)
    
    #Store the width and height
    width, height = im.size
    
    # Setting the points for cropped image
    left = 0
    top = 0
    right = width
    bottom = height-100
    
    #crop the bottom off the image
    im_cropped = im.crop((left, top, right, bottom))
    
    #get new image width and height, this'll make the math easier
    width, height = im_cropped.size
    
    #Prepare rectangle
    draw = ImageDraw.Draw(im_cropped)
    
    #Size of rectangle
    w, h = 200, 100
    
    x0 = 0
    y0 = height - h
    x1 = w
    y1 = height    
    
    shape = [(x0, y0), (x1, y1)]
    draw.rectangle(shape, fill ="black",outline ="black")
    
    output_image_path = Path.cwd().joinpath(output_path,image_path.name)

    # Create the directory if it doesn't exist
    output_image_path.parent.mkdir(parents=True, exist_ok=True)
    
    im_cropped.save(output_image_path)