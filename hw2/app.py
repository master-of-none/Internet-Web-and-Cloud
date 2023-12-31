"""
Building details built using Flask
"""

#import required things.
import flask
from flask.views import MethodView
from index import Index
from enter import Enter
from view import View

#intialise flask.
app = flask.Flask(__name__)


# Add routes such that homepage, view and insert is acheived.
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])
app.add_url_rule('/view',
                 view_func=View.as_view('view'),
                 methods=["GET"])

app.add_url_rule('/enter',
                 view_func=Enter.as_view('enter'),
                 methods=["GET", "POST"])

# Run the program on specified port and on localhost
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
