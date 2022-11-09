from flask import Flask,render_template, request
import ibm_db

app=Flask(__name__)
HOSTNAME = "98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
PORT = 30875
UID = "dpg24841"
PWD = "UNdnXBkgfF7gfffE"
conn = ibm_db.connect('DATABASE=bludb;'
                     f'HOSTNAME={HOSTNAME};'
                     f'PORT={PORT};'
                      'SECURITY=SSL;'
                      'PROTOCOL=TCPIP;'
                     f'UID={UID};'
                     f'PWD={PWD};', '', '')





@app.route("/home")

def home():
   #return "hello guhan"
   return render_template('index.html', msg=None)

@app.route("/about")
def about():
   #return "hello guhan"
   return render_template('about.html')

@app.route("/signup")
def signup():
   #return "hello guhan"
   return render_template('signup.html')

@app.route("/signin")
def signin():
   #return "hello guhan"
   return render_template('signin.html', msg=None)

@app.route("/signinhandler", methods=['POST'])
def signinhandler():
   sql = f"select * from userdata where username='{request.form['username']}' and password='{request.form['password']}';"
   d = ibm_db.fetch_both(ibm_db.exec_immediate(conn, sql))
   if d:
      return render_template('index.html', msg="Successfully Signed in")
   return render_template('signin.html', msg="Wrong Password")


if __name__=='__main__':
   app.run(debug=True)