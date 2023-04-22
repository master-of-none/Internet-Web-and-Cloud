"""
Building details built using Flask
"""
import flask
from flask.views import MethodView
from index import Index
from enter import Enter

app = flask.Flask(__name__)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])


app.add_url_rule('/enter',
                 view_func=Sign.as_view('sign'),
                 methods=["GET", "POST"])
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
