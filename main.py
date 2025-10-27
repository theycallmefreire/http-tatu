from flask import Flask, render_template, abort

app = Flask(__name__)

STATUS_DATA = {
    200: {
        "nome": "OK",
        "descricao": "OK! Requisição bem-sucedida. Tudo certo e protegido, como um tatu-bola!",
        "imagem": "200.jpg"
    },
    404: {
        "nome": "Not Found (Não Encontrado)",
        "descricao": "Não encontrado! O recurso que você procura se escondeu, como um tatu em sua toca. Precisamos proteger seus habitats!",
        "imagem": "404.jpg"
    },
    500: {
        "nome": "Internal Server Error (Erro Interno)",
        "descricao": "Erro Interno! Nosso servidor encontrou um problema. É um alerta crítico, assim como o risco de extinção que muitos tatus enfrentam.",
        "imagem": "500.jpg"
    },
    301: {
        "nome": "Moved Permanently (Movido Permanentemente)",
        "descricao": "Movido Permanentemente! O recurso foi realocado, assim como os tatus que migram para novos habitats em busca de segurança.",
        "imagem": "301.jpg"
    },
    403: {
        "nome": "Forbidden (Proibido)",
        "descricao": "Proibido! Você não tem permissão para acessar este recurso, assim como os tatus que protegem seus territórios.",
        "imagem": "403.jpg"
    },
    # Você pode adicionar mais códigos aqui...
}

@app.route('/')
def pagina_principal():
    """
    Esta é a rota da "página principal".
    Ela renderiza o index.html e passa TODOS os dados para ele.
    """
    # Passamos os dados para o template para ele poder criar a galeria
    return render_template('index.html', codigos=STATUS_DATA)


@app.route('/<int:codigo_status>')
def mostrar_status(codigo_status):
    """
    Esta é a "rota dinâmica" ou "página padrão" que você mencionou.
    Ela captura o número da URL (ex: /404) e usa como variável.
    """
    
    # 1. Procura o código nos nossos dados
    info_codigo = STATUS_DATA.get(codigo_status)

    # 2. Se o código não existir no nosso dicionário, mostramos um erro 404 real.
    if not info_codigo:
        # A função abort() do Flask é a forma correta de retornar um erro HTTP
        abort(404) 

    # 3. Se achamos o código, renderizamos a página 'status.html'
    #    passando APENAS as informações daquele código específico.
    return render_template('status.html', info=info_codigo, codigo=codigo_status)


# Rota para lidar com erros 404 (quando o usuário acessa uma rota que não existe)
@app.errorhandler(404)
def pagina_nao_encontrada(error):
    # Vamos ser espertos: se o usuário digitar uma URL errada,
    # vamos mostrar a NOSSA PRÓPRIA página 404!
    
    # Pegamos os dados do 404
    info_404 = STATUS_DATA.get(404)
    
    # Renderizamos nosso template de status e retornamos o status 404
    return render_template('status.html', info=info_404, codigo=404), 404


if __name__ == '__main__':
    app.run(debug=True)