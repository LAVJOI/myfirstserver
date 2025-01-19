from flask import Blueprint,render_template,redirect,url_for,session,request
from controllers.db_controller import db_controller
from controllers.validation import Validator
from views.view import View

pa_bp = Blueprint('pa', __name__, template_folder="templates")

class Pa(View):

    def __init__(self):
        super().__init__()

    def pa(self):

        self.variable_reset()

        if request.method == "POST":
            response_data = session.get('global_data', None)
            data = dict(request.form)
            userdata_validation = Validator(data).userdata_validator()
            if userdata_validation["username"] and userdata_validation["surname"]:
                data["user_id"] = response_data["user_data"]["id"]
                response_data = db_controller(data, update=True)
                session['global_data'] = response_data
                return redirect(url_for('pa.pa', id = response_data["user_data"]["id"]))
            else:
                return render_template('p_a.html', 
                    valid_name = userdata_validation["username"],
                    valid_surname = userdata_validation["surname"], 
                    ch = True,
                    name = response_data["user_data"]["username"],
                    surname = response_data["user_data"]["surname"]

                )
        
        if request.method == "GET":
            response_data = session.get('global_data', None)
            if request.args.get("id") == None:
                if response_data is not None:
                    return redirect(url_for('pa.pa', id = response_data["user_data"]["id"]))
                else:
                    return redirect(url_for('login.login'))
                
            url_id = request.args.get('id')
            url_id = int(url_id)

            if  response_data is not None: 
            
                if request.args.get('action') == 'delete':
                    self.action_dl = True
                if request.args.get('action') == 'change':
                    self.action_ch = True
                if request.args.get('verif') == 'True':
                    return redirect("/delete")
                
                login_status = response_data["login_status"]
                user_id = response_data["user_data"]["id"]

                if login_status and url_id == user_id :
                    return render_template('p_a.html', name = response_data["user_data"]["username"], 
                                        surname = response_data["user_data"]["surname"], user_id = user_id, 
                                        dl = self.action_dl, ch = self.action_ch,)
                else:
                    return("Вы не авторизованы или пытаетесь получить доступ не к своему аккаунту")
            else:
                return ("404")
                

pa_view = Pa()

pa_bp.add_url_rule(
    "/pa",
    view_func = pa_view.pa, 
    methods = ["GET", "POST"]
)