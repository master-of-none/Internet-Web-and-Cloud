"""
This is used to display the index.html file
"""

#import the required things
from flask import render_template, request
from flask.views import MethodView
from flask import Flask
import gbmodel
app = Flask(__name__)

class Index(MethodView):
    def get(self):
        """
        This function displays the homepage for the app.
        :return: template which displays homepage which is an html file.
        """
        #model = gbmodel.get_model()
        #entries = [dict(bname=row[0], bcode=row[1], bfloor=row[2], closeRoomNumber=row[3], rating=row[4] ) for row in model.select()]
        
        return render_template('index.html')

    def post(self):
        # Handle the POST request here
        ingredients = request.form.get("ingredients")
        # Your code goes here
        
        return render_template('index.html')

app.add_url_rule('/', view_func=Index.as_view('index'))

