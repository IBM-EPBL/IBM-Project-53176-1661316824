from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os 


	

def alert(main_msg):
    mail_from = 'bhavani_a@psrr.edu.in'
mail_to = 'bhavani_a@psrr.edu.in'
msg = MIMEMultipart()
msg['From'] = mail_from
msg['To'] = mail_to
msg['Subject'] = '!Alert Mail On Product Shortage! - Regards'
mail_body = main_msg
msg.attach(MIMEText(mail_body))



engine = create_engine("mysql+pymysql://root@localhost/stock")

db= scoped_session(sessionmaker(bind = engine))
buffersize = 64 * 1024
app=Flask(__name__)

@app.route('/')
def register():
    return render_template('Register.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/productentry')
def productentry():
    return render_template('productentry.html')
@app.route('/view')
def view():
    return render_template('view.html')
@app.route('/image')
def image():
    return render_template('img/background.jpg')
class reg(db.Model):
    Cid = db.Column(db.Integer, primary_key = True)
    Cname = db.Column(db.String(100))
    CAddress = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    Details = db.Column(db.String(100))
    uname = db.Column(db.String(100))
    password = db.Column(db.String(100))
  
    def __init__(self, Cname, CAddress, phone, Details, uname, password):
        self.name = Cname
        self.Cname = Cname
        self.CAddress = CAddress
        self.Details = Details
        self.uname = uname
        self.password = password

if __name__=="__main__":
    app.run(debug=True)
