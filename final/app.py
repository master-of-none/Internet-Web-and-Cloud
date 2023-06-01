import flask
from flask.views import MethodView
from index import Index
from enter import Enter

app = flask.Flask(__name__)

#Adding routes

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET", "POST"])

app.add_url_rule('/enter',
                 view_func=Enter.as_view('enter'))

# Run the program on specified port and on localhost
if __name__ == "__main__":
    app.run(debug=True)


