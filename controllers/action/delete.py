from flask import Blueprint,redirect,session
from controllers.db_controller import db_controller
from controllers.loginstatus_check import login_check


delete_bp = Blueprint("delete", __name__, template_folder="templates")

@delete_bp.route("/delete")
def delete():
    data = session.get('global_data',None)
    login_status = login_check()
    if login_status is not False:
        db_controller(data["user_data"], delete=True)
        session.clear()
        return redirect('/')
    else:
        return ("У вас недостаточно прав для этого действия")