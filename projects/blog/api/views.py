from flask_restful import Resource, reqparse
from flask import jsonify
from projects.blog.models import Posts

# reqparse
posts_parser = reqparse.RequestParser()
posts_parser.add_argument('title', type=str, help="Title is Required", required=True)
posts_parser.add_argument('contents', type=str, help='Contents is Required', required=True)

posts_update = reqparse.RequestParser()
posts_update.add_argument('title', type=str)
posts_update.add_argument('contents', type=str)


# views
class PostList(Resource):
    def get(self):
        posts = Posts.objects()
        return jsonify(posts)

    def post(self, title: str, contents: str):
        args = posts_parser.parse_args()
        posts = Posts(title=args['title'], contents=args['contents'])
        posts.save()
        return posts, 201
