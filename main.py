from flask import Flask, url_for, render_template, redirect
from views import views 

app = Flask(__name__, static_folder='static')

app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)