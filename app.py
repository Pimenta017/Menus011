from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registo')
def registo():
    return render_template('registo.html')

@app.route('/Vehicles')
def Vehicles():
    return render_template('Vehicles.html')

@app.route('/Soldiers')
def Soldiers():
    return render_template('Soldiers.html')

if __name__ == '__main__':
    app.run()

