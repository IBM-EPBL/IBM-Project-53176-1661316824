from flask import Flask,render_template

app=Flask(__name__)

@app.route("/home")

def home():
   #return "hello hemasai"
   return render_template('index.html')

@app.route("/about")
def about():
   #return "hello hemasai"
   return render_template('about.html')

@app.route("/signup")
def signup():
   #return "hello hemasai"
   return render_template('signup.html')

@app.route("/signin")
def signin():
   #return "hello hemasai"
   return render_template('signin.html')

if __name__=='__main__':
   app.run(debug=True)