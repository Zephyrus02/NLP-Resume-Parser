from flask import Flask, request, jsonify
import utils.resume_parser as rp # available functions: parse_pdf, return_path

app = Flask(__name__)

@app.route('/send-file-path', methods=['POST'])
def send_file_path():
    data = request.get_json()
    file_path = data.get('file_path')
    
    if not file_path:
        return jsonify({'error': 'File path not provided'}), 400

    response_string = rp.parse_pdf(file_path)
    file_path = rp.return_path(file_path)

    return jsonify({'message': response_string, 'file_path': file_path})

if __name__ == '__main__':
    app.run(debug=True, port=5001)