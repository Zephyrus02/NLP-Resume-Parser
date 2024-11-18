from flask import Flask, request, jsonify
import utils.resume_parser as rp # available functions: pdfToStr, ResumeParser

app = Flask(__name__)

@app.route('/get-role', methods=['POST'])
def predictRes():
    data = request.get_json()
    text = data.get('text')
    
    if not text:
        return jsonify({'error': 'File not provided'}), 400

    JobRole = rp.ResumeParser(text)
    print("Job Role: ", JobRole)

    return JobRole

# @app.route('/get-courses', methods=['POST'])
# def get_courses():
#     data = request.get_json()
#     text = data.get('text')
    
#     if not text:
#         return jsonify({'error': 'File not provided'}), 400

#     courses = rp.get_recommended_courses(text)

#     return courses

if __name__ == '__main__':
    app.run(debug=True, port=5001)