import os
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.add_font('Urdu', '', '/home/hydra/Desktop/project_llm_shinka_wellafre/fonts/NotoNastaliqUrdu-VariableFont_wght.ttf', uni=True)
        self.set_font('Urdu', '', 14)

    def write_text(self, results: dict):
        for filename, text in results.items():
            self.multi_cell(0, 10, f"--- {filename} ---\n{text}\n\n")

def save_text_to_file(results: dict, txt_path: str, pdf_path: str):
    # Save to TXT
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for filename, text in results.items():
            txt_file.write(f"\n--- {filename} ---\n{text}\n")

    # Save to PDF
    pdf = PDF()
    pdf.write_text(results)
    pdf.output(pdf_path)


# import os
# from fpdf import FPDF

# def save_text_to_file(results: dict, txt_path: str, pdf_path: str):
#     # Save to TXT
#     with open(txt_path, 'w', encoding='utf-8') as txt_file:
#         for filename, text in results.items():
#             txt_file.write(f"\n--- {filename} ---\n{text}\n")

#     # Save to PDF
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     for filename, text in results.items():
#         pdf.multi_cell(0, 10, f"--- {filename} ---\n{text}\n\n")
#     pdf.output(pdf_path)
