import fitz

def parse_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text_content = ""

        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text_content += page.get_text()

        doc.close()

        formatted_text = ' '.join(text_content.split())

        return formatted_text

    except Exception as e:
        error_msg = f"An error occurred while processing the PDF: {e}"
        return error_msg

def return_path(file_path):
    return file_path