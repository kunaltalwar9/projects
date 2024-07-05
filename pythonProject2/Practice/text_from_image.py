from PIL import Image
import pytesseract


image1= r'C:\Users\Kunal Talwar\Pictures\Screenshots\Screenshot (32).png'

obj1= Image.open(image1)
print(pytesseract.image_to_string(obj1))