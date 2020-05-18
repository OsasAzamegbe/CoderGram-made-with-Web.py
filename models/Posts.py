import pymongo
from pymongo import MongoClient


class Posts:
    def __init__(self):

        self.client = MongoClient()
        self.db = self.client.codegram
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_post(self, data):

        post_id = self.Posts.insert({"username": data.username, "post": data.content})
        print("Post Id:", post_id)

        if post_id:
            return True
        else:
            return False

    def get_all_posts(self):
        all_posts = self.Posts.find()
        posts_list = []
        for post in all_posts:
            post['user'] = self.Users.find_one({"username": post["username"]})
            posts_list.append(post)
        return posts_list
