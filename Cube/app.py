from flask import Flask,render_template,redirect,url_for,request,session,g
import sqlite3
import time
from datetime import datetime
app = Flask(__name__)

#Rule1:  Trigger a push notification on very first bill pay event for the user
def rule1(user_id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    sel=cur.execute("Select * from events where user_id={}  and  noun='bill' and verb=='pay'".format(user_id))
    sel_data = cur.fetchall(); 
    if len(sel_data)==1:
        print('Notification')
    conn.close()
    return True


@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' or request.form['password'] == 'admin':
            session['user_id'] = 2
            session['username'] = 'admin'
            return redirect(url_for('admin'))
        elif request.form['username'] == 'user1' or request.form['password'] == 'user1':
            session['user_id'] = 1
            session['username'] = 'user1'
            session['location'] = request.remote_addr
            return redirect(url_for('events'))
        else:
            error = 'Invalid Credentials. Please try again.'
            
    return render_template('login.html', error=error)


@app.route('/payment',methods=['GET', 'POST'])
def payment():
        if request.method=="POST":
            user_id=session['user_id']
            now=datetime.now()
            ts = datetime.timestamp(now)
            ts=str(ts)
            noun='bill'
            verb='pay'
            location= request.remote_addr
            start_time=int(session['start_time'])
            timespent=int(time.time())-start_time
            properties={}
            properties['bank']=request.form['bank']
            properties['value']=request.form['amount']
            properties=str(properties)
            ins_statment='INSERT INTO events (user_id,ts,noun,verb,location,timespent,properties) VALUES ({},"{}","{}","{}","{}",{},"{}")'.format(user_id,ts,noun,verb,location,timespent,properties)
            print(ins_statment)
            conn = sqlite3.connect('database.db')
            ins=conn.execute(ins_statment)
            conn.commit()
            conn.close()

            return redirect(url_for('events'))

        return render_template('payment.html')


@app.route('/',methods=['GET', 'POST'])
def events():
    if request.method=="POST":
        if request.form['event'] == 'pay':
            session['start_time']=time.time()
            return redirect(url_for('payment'))
        return render_template('events.html')


    return render_template('events.html')


@app.route('/admin')
def admin():
    return render_template('operator.html')

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'abcdefgh'
    app.run(host='0.0.0.0')
