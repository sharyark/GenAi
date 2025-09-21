import os
from src.ocr_processor import extract_text_from_images
from src.file_writer import save_text_to_file

if __name__ == "__main__":
    image_folder = 'pic_data'
    output_folder = 'data_output'
    os.makedirs(output_folder, exist_ok=True)

    txt_output = os.path.join(output_folder, 'output.txt')
    pdf_output = os.path.join(output_folder, 'output.pdf')

    print("🔍 Extracting Urdu text from images...")
    results = extract_text_from_images(image_folder)

    print("📝 Saving text to TXT and PDF...")
    save_text_to_file(results, txt_output, pdf_output)

    print("✅ Done! Text saved in data_output folder.")
