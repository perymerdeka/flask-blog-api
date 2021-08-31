from flask_restful import Resource, reqparse

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
        pass

    def post(self):
        posts = Posts(title='Test Data', contents='This Content')
        posts.save()
