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
        entries = [dict(id=row[0], title=row[1]) for row in model.select()]
        return render_template('view.html', entries = entries)

