from flask import Flask

def create_app():
    app = Flask(__name__)
    #todo: FLEX-2 - move this so the key won't be in github
    app.config['SECRET_KEY'] = 'opieupsmadfa4j3rlemfapoq83japefwoewsfjapo4ifafj'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app