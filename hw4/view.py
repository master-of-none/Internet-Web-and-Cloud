"""
This file displays the values from the database.
"""

# import required things.
from flask import render_template
from flask.views import MethodView
import gbmodel

class View(MethodView):
    def get(self):
        """
        This fumction is used to render the view.html file and display the entries when we click the 'view' link.
        :return: renders template view.html and displays the entries from database.
        """
        model = gbmodel.get_model()
        entries = [dict(bname=row[0], bcode=row[1], bfloor=row[2], closeRoomNumber=row[3], rating=row[4] ) for row in model.select()]
        return render_template('view.html', entries = entries)
