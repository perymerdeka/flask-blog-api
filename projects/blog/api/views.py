from flask_restful import abort, fields, marshal_with, Resource, reqparse
from flask import jsonify
from projects.blog.models import Posts

# reqparse
posts_parser = reqparse.RequestParser()
posts_parser.add_argument('title', type=str, help="Title is Required", required=True)
posts_parser.add_argument('contents', type=str, help='Contents is Required', required=True)

posts_update = reqparse.RequestParser()
posts_update.add_argument('title', type=str)
posts_update.add_argument('contents', type=str)

# resource fields
resource_fields = {
    'id': fields.String,
    'title': fields.String,
    'contents': fields.String
}


# views
class PostListView(Resource):
    def get(self):
        posts = Posts.objects()
        return jsonify(posts)

    @marshal_with(resource_fields)
    def post(self):
        args = posts_parser.parse_args()
        posts = Posts(title=args['title'], contents=args['contents'])
        posts.save()
        return jsonify({'Messages': 'Data Posted Successfullly'}), 201


class PostDetailView(Resource):

    @marshal_with(resource_fields)
    def get(self, post_id: str):
        post = Posts.objects.get(id=post_id)
        if not post:
            abort(404, message=f"Post with id: {post_id} not found")
        return post

    @marshal_with(resource_fields)
    def put(self, post_id: str):
        args = posts_update.parse_args()
        if args['title']:
            Posts.objects.get(id=post_id).update(title=args['title'])
        if args['contents']:
            Posts.objects.get(id=post_id).update(title=args['contents'])
        return jsonify(Posts.objects.get(_id=post_id).first()), 200

    def delete(self, post_id: str):
        posts = Posts.objects(id=post_id)
        posts.delete()
        return jsonify({"message": f"Post with id {post_id} Deleted"}), 204
