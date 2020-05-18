import web
from models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/checklogin', 'CheckLogin',
    '/post-activity', 'PostActivity',
    '/profile', 'Profile'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"user": None})
session_data = session._initializer

render = web.template.render('views/templates/', base="MainLayout",
                             globals={"session": session_data, "current_user": session_data["user"]})
# Classes/Routes


class Home:
    def GET(self):
       # data = type('obj', (object,), {"username": "osasinator", "password": "1234"})

        post_model = Posts.Posts()
        posts = post_model.get_all_posts()
        return render.Home(posts)


class Profile:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_posts()
        post_profile = []
        if session_data['user'] is not None:
            for post in posts:
                if post['username'] == session_data['user']['username']:
                    post_profile.append(post)
        return render.Profile(post_profile)


class Register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        check = reg_model.check_username(data.username)
        if check:
            reg_model.insert_user(data)
            return "success"
        elif check is False:
            return "fail"


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        is_correct = login.verify_user(data)

        if is_correct:
            session_data["user"] = is_correct
            return is_correct

        return "error"


class PostActivity:
    def POST(self):
        data = web.input()
        post = Posts.Posts()
        data.username = session_data["user"]["username"]
        new_post = post.insert_post(data)
        if new_post:
            return 'success'


class Logout:
    def GET(self):
        session["user"] = None
        session_data["user"] = None
        session.kill()
        return "success"


if __name__ == '__main__':
    app.run()
