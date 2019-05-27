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

@app.route('/Veiculos')
def Veiculos():
    return render_template('Veiculos.html')

@app.route('/Soldados')
def Soldados():
    return render_template('Soldados.html')

@app.route('/Galo')
def Galo():
    return render_template('Galo.html')

if __name__ == '__main__':
    app.run(debug=True)

