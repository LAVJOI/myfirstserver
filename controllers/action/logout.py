from flask import Blueprint,redirect,url_for,session
from controllers.loginstatus_check import login_check

logout_bp = Blueprint("logout", __name__, template_folder="templates")

@logout_bp.route("/logout")
def logout():
    login_status = login_check()
    if login_status is not False:
        session.clear()
        return redirect(url_for('index.index'))
    else:
        return redirect(url_for('login.login'))
    