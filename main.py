from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = 'abubakar'


@app.route('/')
def login():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
