from flask import Flask, render_template

from test import my_var

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', my_var = my_var)

@app.route('/about/')
def about():
    with  open(r"test.txt") as f:
        s = f.read()
    return render_template('about.html', s = s)

if __name__ == '__main__':
    app.run(debug=True)
