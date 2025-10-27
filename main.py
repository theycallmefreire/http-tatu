from flask import Flask, render_template, abort
from data import STATUS_DATA

app = Flask(__name__)


@app.route('/')
def pagina_principal():
    return render_template('index.html', codigos=STATUS_DATA)


@app.route('/<int:codigo_status>')
def mostrar_status(codigo_status):    
    info_codigo = STATUS_DATA.get(codigo_status)
    if not info_codigo:
        abort(404) 
    return render_template('status.html', info=info_codigo, codigo=codigo_status)

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    info_404 = STATUS_DATA.get(404)
    return render_template('status.html', info=info_404, codigo=404), 404


if __name__ == '__main__':
    app.run(debug=True)