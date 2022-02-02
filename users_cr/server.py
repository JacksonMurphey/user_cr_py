from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)


@app.route('/users')
def index():
    users = User.get_all()
    return render_template('read.html', users=users)

@app.route('/users/new')
def createUser():

    return render_template('create.html')


@app.route('/create', methods=['POST'])
def new_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        
    }
    
    User.save(data)
    return redirect('/users')


    
if __name__=='__main__':
    app.run(debug=True)