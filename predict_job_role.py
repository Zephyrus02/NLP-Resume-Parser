import tensorflow as tf
from transformers import TFBertForSequenceClassification, BertTokenizer

# Define job categories directly in the script
job_categories = ["Advocate", "Arts", "Automation Testing", "Blockchain", "Business Analyst", "Civil Engineer", "Data Science", "Database", "DevOps Engineer", "DotNet Developer", "ETL Developer", "Electrical Engineering", "HR", "Hadoop", "Health and fitness", "Java Developer", "Mechanical Engineer", "Network Security Engineer", "Operations Manager", "PMO", "Python Developer", "SAP Developer", "Sales", "Testing", "Web Designing"]

# Load the BERT model and tokenizer (adjust paths to your model and tokenizer folders)
model = TFBertForSequenceClassification.from_pretrained('bert_resume_classification_model')
tokenizer = BertTokenizer.from_pretrained('bert_tokenizer')

def predict_job_role(resume_text, model, tokenizer, job_categories, max_length=512):

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

#test
parsed_resume_text = "Sahil Khodke Nagpur, Maharashtra 7218613667 | sahil.khodke12@gmail.com Objective: A self-motivated and analytical B.Tech student in Computer Science Engineering specializing in Cyber Physical Systems, seeking a dynamic role in International Capital Markets. Keen on applying quantitative analysis, decision-making, and research skills to develop and execute trading strategies for the firm. Education: Vellore Institute of Technology, Chennai, TN B.Tech in Computer Science Engineering with Specialization in Cyber Physical Systems | Expected 2025 St. Paul Junior College, Nagpur, MH 12th (State Board) | 2021 The Swaminarayan School, Nagpur, MH 10th (CBSE) | 2019 Skills: • Quantitative Analysis: Strong math aptitude with experience in analyzing complex data sets and deriving insights. • Technical Skills: C, C++, Java, MySQL, PHP, Power BI, Advanced Excel • Risk Management: Proficient in assessing and managing risks to optimize performance and outcomes. • Financial Acumen: Understanding of financial markets, economic theories, and their application in capital markets. • Problem Solving & Critical Thinking: Quick thinker with proven ability to make independent decisions in competitive environments. • Market Research: Experience in researching and developing strategies using data, trends, and market sentiment analysis. Experience: K-Star Technology | May 2024 - June 2024 Web Developer Intern • Optimized client websites utilizing PHP, HTML, CSS, and JavaScript, resulting in a 40% improvement in page load times. • Developed strong problem-solving skills by identifying and rectifying issues to improve user satisfaction. Alpha Computer Academy, Nagpur IT Manager • Oversaw and managed IT operations, including software, networking, and hardware, ensuring seamless system performance. • Gained experience in managing multiple tasks under pressure, enhancing operational efficiency. Projects: • IoT-Driven Crop Watering System Designed an automatic irrigation system based on real-time data, honing skills in data analysis and real-time decision-making. Relevant Skill: Data analysis and resource optimization. • IoT-Based RFID Attendance System Automated attendance tracking using RFID, showcasing problem-solving and data management capabilities. • V-Maps for Newcomers Created a navigation tool for university campuses, demonstrating leadership and technical skills. • E-Commerce Website for Clothing Brand Developed a functional online shopping platform using HTML, CSS, and JavaScript, which improved customer engagement. Certifications: • Amazon Web Services (AWS) • C, C++, Java, SQL Training – IIT Bombay Extracurricular Activities: • National Level Hockey Player o Played for Maharashtra in the Khelo India Youth Games. o Served as captain for the district and university teams, demonstrating leadership and teamwork skills. o Awarded Best Emerging Player in 2022. Additional Strengths: • Entrepreneurial mindset with a readiness to work in a fast-paced, competitive environment. • Ability to quickly assimilate data, analyze market trends, and make informed decisions. • Strong work ethic and commitment to professional growth."  # Replace with actual parsed resume text
predicted_job_role = predict_job_role(parsed_resume_text, model, tokenizer, job_categories)

print(f"Predicted job role: {predicted_job_role}")
