"""
This contains all the routes which are needed for the application.
"""

import flask
from flask.views import MethodView
from index import Index
from enter import Enter
from nutrients import Nutrients
from enter import Favorites
from view import View

app = flask.Flask(__name__)

#Adding routes

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET", "POST"])

app.add_url_rule('/enter',
                 view_func=Enter.as_view('enter'))

app.add_url_rule('/nutrients',
                 view_func=Nutrients.as_view('nutrients'))

app.add_url_rule('/favorites',
                 view_func=Favorites.as_view('favorites'),
                 methods=["POST"])

app.add_url_rule('/view',
                 view_func=View.as_view('view'),
                 methods=["GET"])

# Run with default Flask port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


