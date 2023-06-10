"""
This is used to display the index.html file
"""

#import the required things
from flask import render_template, request
from flask.views import MethodView
from flask import Flask
app = Flask(__name__)

class Index(MethodView):
    def get(self):
        """
        This function displays the homepage for the app.
        :return: template which displays homepage which is an html file.
        """
        
        return render_template('index.html')

    def post(self):
        ingredients = request.form.get("ingredients")
        return render_template('index.html')

app.add_url_rule('/', view_func=Index.as_view('index'))

