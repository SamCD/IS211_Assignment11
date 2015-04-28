from flask import Flask, render_template
from flask import request,redirect,url_for
import re
app = Flask(__name__)

todo = []
err_msg = ''

@app.route('/')
def print_list():
    return render_template('index.html',todo=todo,err_msg=err_msg)

@app.route('/submit', methods = ['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    if re.search(r'@\w*\.\w',email):
        if priority in ('high','medium','low'):
            todo.append(task + ' for ' + email + '. Priority: ' + priority)
        else:
            err_msg = 'Please select a priority level'
    else:
        err_msg = 'Please enter a valid e-mail'
    return redirect(url_for('print_list'))

@app.route('/clear', methods = ['POST'])
def clear():
    del todo[:]
    return redirect(url_for('print_list'))
    


if __name__ == '__main__':
    app.run()
