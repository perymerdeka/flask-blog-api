from flask import Blueprint
from flask_restful import Api

# API Blueprint
from projects.blog.api.views import PostListView, PostDetailView

blog_api_blueprint = Blueprint('blog', __name__, template_folder='templates', static_folder='static')
blog_api = Api(blog_api_blueprint)

# routes
blog_api.add_resource(PostListView, "/blog/api/posts/")
blog_api.add_resource(PostDetailView, "/blog/api/posts/<post_id>/")
