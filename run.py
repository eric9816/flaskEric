from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='Главная')


@app.route('/naruto_page')
def naruto_page():
    return render_template('naruto_page.html')


@app.route('/bleach_page')
def bleach_page():
    return render_template('bleach_page.html')


@app.route('/jojo_page')
def jojo_page():
    return render_template('jojo_page.html')


@app.route('/onepunch_page')
def onepunch_page():
    return render_template('onepunch_page.html')


@app.route('/blackclover_page')
def blackclover_page():
    return render_template('blackclover_page.html')


@app.route('/mob_page')
def mob_page():
    return render_template('mob_page.html')


if __name__ == '__main__':
    app.run(debug=True)
