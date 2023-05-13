"""
This file is used to enter the values to database.
"""

#Import required things.
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Enter(MethodView):
    def get(self):
        """
        This function is used to render the enter.html template
        :return: enter.html file which contains front end to enter the details to database.
        """
        return render_template('enter.html')

    def post(self):
        """
        This function basically inserts the valye to database, this executes when data is entered and enter
        button is clicked.
        :return: After entering, this will return the homepage of the application.
        """
        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['code'], request.form['floor'], request.form['closeRoomNumber'], request.form['rating'])
        return redirect(url_for('index'))

