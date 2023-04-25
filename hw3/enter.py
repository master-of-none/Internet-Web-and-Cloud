from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Enter(MethodView):
    def get(self):
        return render_template('enter.html')

    def post(self):
        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['code'], request.form['floor'], request.form['closeRoomNumber'], request.form['rating'])
        return redirect(url_for('index'))

