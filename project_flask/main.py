from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
       return render_templates('index.html')

@app.route('/usuario/<usuario>')
def usuario(nome):
       return nome

@app.route('/contatos')
def index():
       return render_templates('contatos.html',
       nome="lucas",
       email="adm.adm@gmail.com")
def index():
       return 'Olá Mundo!'

if __name__ == '__main__':
       app.run(debug=True)