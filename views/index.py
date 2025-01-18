from flask import Blueprint,render_template,redirect,url_for,session
from controllers.loginstatus_check import login_check
index_bp = Blueprint('index', __name__, template_folder='templates')

@index_bp.route("/")
def index():
    response_data = session.get("global_data", None)
    login_status = login_check()
    if login_status is False:
        return render_template('main.html')
    else:
        return redirect(url_for('pa.pa', id = response_data["user_data"]["id"]))