from flask import Blueprint, render_template, redirect, url_for, request, session
from controllers.db_controller import  db_controller
from controllers.loginstatus_check import login_check
from controllers.validation import Validator
from views.view import View
from loguru import logger


registration_bp = Blueprint("registration", __name__, template_folder="template")

class Registration(View):
    
    def __init__():
        super().__init__()


    @registration_bp.route('/registration', methods = ["GET", "POST"])
    def registration():
        response_data = session.get("global_data", None)
        login_status = login_check()
        if login_status is False:
            if request.method == 'POST':
                data = dict(request.form)
                userdata_validation = Validator(data).userdata_validator()
                accoutingdata_validation = Validator(data).accoutingdata_validator()
                if userdata_validation["username"] and userdata_validation["surname"] and accoutingdata_validation["email"] and accoutingdata_validation["password"]:
                    response_data = db_controller(data, registration=True)
                    if response_data["login_status"]:
                        session['global_data'] = response_data
                        return redirect(url_for('pa.pa', id = response_data["user_data"]["id"]))
                    else: 
                        return render_template('bad_data_registration.html')
                else:
                    return render_template(
                        'registration.html', 
                        valid_name = userdata_validation["username"],
                        valid_surname = userdata_validation["surname"],
                        valid_email = accoutingdata_validation["email"],
                        valid_password = accoutingdata_validation["password"]
                    )
            if request.method == "GET":
                return render_template('registration.html')
        else:
            return redirect(url_for('pa.pa', id = response_data["user_data"]["id"]))
        
