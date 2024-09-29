from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.models import File

client_bp = Blueprint('client', __name__)

@client_bp.route('/files', methods=['GET'])
@jwt_required()
def list_files():
    current_user = get_jwt_identity()
    if current_user['role'] != 'Client':
        return jsonify({'message': 'Unauthorized'}), 403

    files = File.query.all()
    output = []
    for file in files:
        output.append({'file_name': file.file_name, 'uploaded_at': file.uploaded_at})
    return jsonify({'files': output}), 200
