import fitz
import tensorflow as tf
from transformers import TFBertForSequenceClassification, BertTokenizer

def pdfToStr(pdf_path):
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

def ResumeParser(resume_text):

    max_length=512
    # Define job categories directly in the script
    job_categories = ["Advocate", "Arts", "Automation Testing", "Blockchain", "Business Analyst", "Civil Engineer", "Data Science", "Database", "DevOps Engineer", "DotNet Developer", "ETL Developer", "Electrical Engineering", "HR", "Hadoop", "Health and fitness", "Java Developer", "Mechanical Engineer", "Network Security Engineer", "Operations Manager", "PMO", "Python Developer", "SAP Developer", "Sales", "Testing", "Web Designing"]

    # Load the BERT model and tokenizer (adjust paths to your model and tokenizer folders)
    model = TFBertForSequenceClassification.from_pretrained('bert_resume_classification_model')
    tokenizer = BertTokenizer.from_pretrained('bert_tokenizer')

    # Tokenize the input resume text
    inputs = tokenizer(
        text=resume_text,
        add_special_tokens=True,
        padding=True,
        truncation=True,
        max_length=max_length,
        return_tensors='tf',
        return_attention_mask=True,
        return_token_type_ids=False
    )

    # Get input_ids and attention_mask
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    # Make prediction
    predictions = model(input_ids, attention_mask=attention_mask, training=False)
    predicted_class = tf.argmax(predictions.logits, axis=1).numpy()[0]

    predicted_job_role = job_categories[predicted_class]

    return predicted_job_role