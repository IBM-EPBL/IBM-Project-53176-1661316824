from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


if __name__ == '__main__':
  app.config['SECRET_KEY'] = '1234567890'
  app.run(host = '0.0.0.0')