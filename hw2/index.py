from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(bname=row[0], bcode=row[1], bfloor=row[2], closeRoomNumer=row[3], rating=row[4] ) for row in model.select()]
        return render_template('index.html', entries = entries)
