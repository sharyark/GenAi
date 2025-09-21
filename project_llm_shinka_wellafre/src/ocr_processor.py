import easyocr
import os

def extract_text_from_images(folder_path: str, lang='ur') -> dict:
    reader = easyocr.Reader([lang])
    results = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(folder_path, filename)
            text_list = reader.readtext(img_path, detail=0)
            results[filename] = "\n".join(text_list).strip()
    return results





# import pytesseract
# from PIL import Image
# import os

# def extract_text_from_images(folder_path: str, lang='urd') -> dict:
#     results = {}
#     for filename in os.listdir(folder_path):
#         if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#             img_path = os.path.join(folder_path, filename)
#             img = Image.open(img_path)
#             text = pytesseract.image_to_string(img, lang=lang)
#             results[filename] = text.strip()
#     return results
