from flask import Flask, url_for, render_template, redirect, request
from views import views 
# import pypyodbc as odbc 
# import pandas as pd 
# import sys
# from credential import username, password

app = Flask(__name__, static_folder='static')
app.secret_key = "hello"
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
    
