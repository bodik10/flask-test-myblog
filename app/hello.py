from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    f = open(r"test.txt", "a+")
    f.write("spam\n")
    f.close()
    return render_template('home.html')

@app.route('/about/')
def about():
    with  open(r"test.txt") as f:
        s = f.read()
    return render_template('about.html', s = s)

if __name__ == '__main__':
    app.run(debug=True)
