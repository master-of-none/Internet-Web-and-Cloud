"""
This is used to display the index.html file
"""

#import the required things
from flask import render_template
from flask.views import MethodView
import gbmodel


class Index(MethodView):
    def get(self):
        """
        This function displays the homepage for the app.
        :return: template which displays homepage which is an html file.
        """
        #model = gbmodel.get_model()
        #entries = [dict(bname=row[0], bcode=row[1], bfloor=row[2], closeRoomNumber=row[3], rating=row[4] ) for row in model.select()]
        
        return render_template('index.html')
