import flask
from flask.views import MethodView
from index import Index
from enter import Enter
from nutrients import Nutrients

app = flask.Flask(__name__)

#Adding routes

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET", "POST"])

app.add_url_rule('/enter',
                 view_func=Enter.as_view('enter'))

app.add_url_rule('/nutrients',
                 view_func=Nutrients.as_view('nutrients'))
# Run the program on specified port and on localhost
if __name__ == "__main__":
    app.run(debug=True)


