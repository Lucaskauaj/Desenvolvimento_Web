from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/segundo')
def segundo():
    return render_template('segundo.html')

@app.route('/terceiro')
def terceiro():
    return render_template('terceiro.html')

@app.route('/quarto')
def quarto():
    return render_template('quarto.html')


@app.route('/recebedados', methods=['GET'])
def recebedados():
    nome = request.args["nome"]
    email = request.args["email"]
    telefone = request.args["telefone"]
    idade = request.args["idade"]
    return "{} - <br> {}- {} - {}".format(nome, email, idade, telefone)
                  

if __name__ == '__main__':
    app.run(debug=True)
