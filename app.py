from flask import Flask, request, jsonify
import utils.resume_parser as rp # available functions: pdfToStr, ResumeParser

app = Flask(__name__)

@app.route('/send-file-path', methods=['POST'])
def send_file_path():
    data = request.get_json()
    file_path = data.get('file_path')
    
    if not file_path:
        return jsonify({'error': 'File path not provided'}), 400

    response_string = rp.pdfToStr(file_path)
    JobRole = rp.ResumeParser(response_string)

    return JobRole

@app.route('/get-courses', methods=['POST'])
def get_courses():
    data = request.get_json()
    file_path = data.get('file_path')
    
    if not file_path:
        return jsonify({'error': 'File path not provided'}), 400

    response_string = rp.pdfToStr(file_path)
    courses = rp.get_recommended_courses(response_string)

    return courses

if __name__ == '__main__':
    app.run(debug=True, port=5001)