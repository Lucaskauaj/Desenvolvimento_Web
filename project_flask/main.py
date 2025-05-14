from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
       return render_template('index.html')

@app.route('/usuario/<usuario>')
def usuario(usuario):
       return render_template('usuario.html')

@app.route('/contatos')
def contatos():
       return render_template('contatos.html')


if __name__ == '__main__':
       app.run(debug=True)