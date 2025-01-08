from flask import Flask, render_template, redirect, url_for, session
from flask import request
from db import Database

app = Flask(__name__)
app.secret_key = 'erpjgpeprgrhdfi43800wha;daanv'

@app.route('/')
def main():
    response_data = session.get('global_data', None)
    if response_data == None:
        login_status = None
    else:
        login_status = response_data[0]
    print(login_status)
    if login_status is False or login_status is None:
        return render_template('main.html')
    else:
        u = url_for('pa',id = response_data[1][0][2])
        print("urla ", u)
        return redirect(url_for('pa', id = response_data[1][0][2]))

@app.route('/registration', methods = ["GET", "POST"])
def registration():
    response_data = session.get('global_data', None)
    if response_data == None:
        login_status = None
    else:
        login_status = response_data[0]
    if login_status is False or login_status is None:
        if request.method == 'POST':
            data = dict(request.form)
            template = Database().registration_db(data)
            return render_template(template)
        else:
            return render_template('registration.html')
    else:
        return redirect(url_for('pa', id = response_data[1][0][2]))

@app.route('/login', methods = ["GET", "POST"])
def login():
    response_data = session.get('global_data', [False])
    if response_data == None:
        login_status = None
    else:
        login_status = response_data[0]
    if login_status is False or login_status is None:
        if request.method == 'POST':
            data = dict(request.form)
            response_data = Database().login(data)
            login_status = response_data
            if login_status == False: 
                return render_template("bad_data_login.html")
            else: 
                session['global_data'] =  response_data
                return redirect(url_for('pa', id = response_data[1][0][2]))
        else:
            return render_template('login.html')
    else:
        return redirect(url_for('pa', id = response_data[1][0][2]))

   
@app.route('/pa', methods = ['GET', 'POST']) 
def pa():
        
        if request.method == "POST":
            response_data = session.get('global_data', None)
            data = [dict(request.form), response_data[1][0][2]]
            session['global_data'] = Database().change(data)
            return redirect(url_for('pa', id = response_data[1][0][2]))
        else:
            response_data = session.get('global_data', None)
            action_dl = False
            action_ch = False
            if request.args.get("id") == None:
                if response_data is not None:
                    return redirect(url_for('pa', id = response_data[1][0][2]))
                else:
                    return("Вы не авторизованы или пытаетесь получить доступ не к своему аккаунту")
            url_id = int(request.args.get('id'))
            print(type(url_id))
            verif = request.args.get('verif')

            if  response_data is not None: 
                if request.args.get('action') == 'delete':
                    action_dl = True
                if request.args.get('action') == 'change':
                    action_ch = True
                if verif == "True":
                    return redirect("/delete")
                login_status = response_data[0]
                user_id = response_data[1][0][2]
                print(url_id)
                print(user_id)
                print(login_status)
                if login_status and url_id == user_id :
                    user_data = response_data[1]
                    user_surname = user_data[0][0]
                    user_name = user_data[0][1]
                    return render_template('p_a.html', name = user_name, 
                                        surname = user_surname, user_id = user_id, 
                                        dl = action_dl, ch = action_ch)
                else:
                    return("Вы не авторизованы или пытаетесь получить доступ не к своему аккаунту")
            else:
                return ("404")

@app.route('/logout')
def logout():
    response_data = session.get('global_data',[False])
    if response_data == None:
        login_status = None
    else:
        login_status = response_data[0]
    if login_status is not False or login_status is not None:
        session.clear()
        return redirect(url_for('main'))
    else:
        return redirect(url_for('login'))
    
@app.route('/delete')
def delete():
    response_data = session.get('global_data',[False])
    print("check")
    if response_data == None:
        login_status = None
    else:
        login_status = response_data[0]
    if login_status is not False or login_status is not None:
        user_id = response_data[1][0][2]
        Database().delete(user_id)
        session.clear()
        return redirect('/')
    else:
        return ("У вас недостаточно прав для этого действия")


if __name__ == '__main__':
    
    Database().create()
    app.run(debug = True)
