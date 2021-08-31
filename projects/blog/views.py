from flask import Blueprint, jsonify

blog_blueprint = Blueprint('blog', __name__, template_folder='templates', static_folder='static')


# route
@blog_blueprint.route('/')
def home():
    message: dict = {'Blog List Page': 'This Is Blog List Page'}
    return jsonify(message)
