from flask import Blueprint


from controllers.doctor_controller import create_doctor, get_doctors
doctor_bp = Blueprint('doctor_route', __name__, url_prefix='/doctors')


doctor_bp.route('/', methods=['GET']) (get_doctors)
# doctor_bp.route('/<int:task_id>', methods=['GET']) (get_todo)
# doctor_bp.route('/<int:task_id>', methods=['PUT']) (update_todo)
# doctor_bp.route('/<int:task_id>', methods=['DELETE']) (delete_todo)
doctor_bp.route('/', methods=['POST']) (create_doctor)
