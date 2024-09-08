from flask import Flask, request, jsonify
from marker import extract  # Import your extraction functionality

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    pdf_file = request.files['file']
    task_id = extract.start_processing(pdf_file)
    return jsonify({'task_id': task_id}), 202

@app.route('/status/<task_id>', methods=['GET'])
def status(task_id):
    status = extract.check_status(task_id)
    return jsonify({'status': status})

@app.route('/images/<task_id>', methods=['GET'])
def images(task_id):
    images = extract.get_images(task_id)
    return jsonify({'images': images})

@app.route('/info/<task_id>', methods=['GET'])
def info(task_id):
    info = extract.get_info(task_id)
    return jsonify({'info': info})

if __name__ == '__main__':
    app.run(debug=True)
