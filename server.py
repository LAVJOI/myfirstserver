from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv

from controllers.action.delete import delete_bp
from views.index import index_bp
from views.login import login_bp
from controllers.action.logout import logout_bp
from views.pa import pa_bp
from views.registration import registration_bp

from models.dbms.load_tables import load_models
from models.dbms.tables.user_list import create_user_list

app = Flask(__name__)
load_dotenv(find_dotenv())
app.secret_key = os.environ["SECRET_KEY"]

app.register_blueprint(delete_bp)
app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(pa_bp)
app.register_blueprint(registration_bp)



if __name__ == '__main__':
    load_models(create_user_list())
    app.run(host='0.0.0.0', port=5000, debug = True)





