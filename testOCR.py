from PIL import Image
import pytesseract

text=pytesseract.image_to_string(Image.open('1.png'),lang='chi_sim')