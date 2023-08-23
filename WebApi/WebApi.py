import os
import uuid
import datetime
import json
from flask import Flask, request, jsonify
import glob
app = Flask(__name__)
UPLOADS_FOLDER = os.environ.get("UPLOADS_FOLDER_PATH")
OUTPUTS_FOLDER = os.environ.get("OUTPUTS_FOLDER_PATH")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file attached'}), 400

    uid = str(uuid.uuid4())
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"{file.filename}_{timestamp}_{uid}"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return jsonify({'uid': uid}), 200


@app.route('/status/<string:uid>', methods=['GET'])
def get_upload_status(uid):
    for file_path in glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], f"*_{uid}")):
        filename = os.path.basename(file_path)
        timestamp = filename.split('_')[1]
        original_filename = '_'.join(filename.split('_')[:-2])
        status = 'done'
        explanation = None

        with open(file_path, 'r') as file:
            try:
                explanation = json.load(file)
            except json.JSONDecodeError:
                pass

        return jsonify({
            'status': status,
            'filename': original_filename,
            'timestamp': timestamp,
            'explanation': explanation
        })

    return jsonify({
        'status': 'not found',
        'filename': None,
        'timestamp': None,
        'explanation': None
    }), 404


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(OUTPUTS_FOLDER):
        os.makedirs(OUTPUTS_FOLDER)
    app.run(debug=True)
