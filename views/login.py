from flask import Blueprint,render_template,redirect,url_for,session,request
from controllers.db_controller import db_controller
from controllers.loginstatus_check import login_check 
from controllers.validation import Validator
from views.view import View

login_bp=Blueprint("login", __name__, template_folder="template")

class Login(View):

    def __init__(self):
        super().__init__()


    @login_bp.route('/login', methods = ["GET", "POST"])
    def login():
        response_data = session.get("global_data", None)
        login_status = login_check()
        if login_status is False:
            if request.method == 'POST':
                data = dict(request.form)
                accoutingdata_validation = Validator(data).accoutingdata_validator()
                if accoutingdata_validation["email"]:
                    response_data = db_controller(data, login=True)
                    login_status = response_data["login_status"]
                    if login_status == False: 
                        return render_template("bad_data_login.html")
                    else: 
                        session['global_data'] =  response_data
                        return redirect(url_for('pa.pa', id = response_data["user_data"]["id"]))
                else:
                    return render_template(
                        'login.html', 
                        valid_email = accoutingdata_validation["email"] 
                        )
            else:
                return render_template('login.html')
        else:
            return redirect(url_for('pa.pa', id = response_data["user_data"]["id"]))
        
