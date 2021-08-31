from flask import Blueprint
from flask_restful import Api

# API Blueprint
from projects.blog.api.views import PostList

blog_blueprint = Blueprint('blog', __name__, template_folder='templates', static_folder='static')
blog_api = Api(blog_blueprint)

# routes
blog_api.add_resource(PostList, "/")
