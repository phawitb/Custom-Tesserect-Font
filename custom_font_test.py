import pytesseract
from PIL import Image

def custom_tess(image_path):

    custom_tessdata_path = 'model/model'
    image = Image.open(image_path)

    # Resize the image
    new_width = int(image.width * 0.7)
    new_height = int(image.height * 0.7)
    image = image.resize((new_width, new_height))
    
    # Perform OCR using the custom trained data for Thai language
    text = pytesseract.image_to_string(image, lang='mytha+eng', config=f'--tessdata-dir "{custom_tessdata_path}"')
    
    return text

image_path = 'test_data/Cocoa-1.png'
text = custom_tess(image_path)

print(text)
