# HTTP Tatu 🐾

Um projeto web que associa códigos de status HTTP a imagens de tatus. Inspirado no `http.cat` e `http.dog`, este app usa Python e Flask para transformar cada erro ou sucesso em um lembrete visual sobre a importância de proteger estes animais.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-black?logo=flask)

---

## A Causa: Por que Tatus?

Enquanto projetos como `http.cat` e `http.dog` focam no humor, o **HTTP Tatu** tem uma missão: **conscientização**.

Cada código de status, seja um "OK" (200) ou um "Not Found" (404), é uma oportunidade para destacar a importância da preservação dos tatus. Estes animais, tão significativos para a fauna brasileira, enfrentam sérios riscos, como a perda de habitat e a caça.

Este projeto é um pequeno lembrete de que podemos usar a tecnologia, mesmo em projetos de estudo, para trazer visibilidade a causas importantes.

## Demonstração

<img width="757" height="643" alt="image" src="https://github.com/user-attachments/assets/ea6ff8e1-189c-4107-a524-41c454a72c6a" />


### Galeria Principal
A página inicial (`/`) exibe todos os códigos de status cadastrados, permitindo uma visualização rápida da galeria e suas descrições.

<img width="1489" height="885" alt="image" src="https://github.com/user-attachments/assets/4ff5e595-1844-4691-bbd5-3421cb9116f5" />


### Página de Status
Cada código possui uma página dedicada (ex: `/404`) que mostra a imagem em tamanho maior e a descrição daquele status, sempre com a temática da preservação.

<img width="763" height="576" alt="image" src="https://github.com/user-attachments/assets/c9d50305-6efb-4074-8705-ac5300012359" />


## Funcionalidades

* **Galeria de Códigos:** Uma página inicial (`/`) que lista todos os códigos de status implementados.
* **Rotas Dinâmicas:** Acesso a cada código individualmente através de rotas dinâmicas (ex: `/200`, `/404`, `/500`).
* **Templates Jinja2:** Uso de um template base (`base.html`) para criar um layout consistente em todo o site.
* **Página de Erro Personalizada:** O app usa sua própria página de 404 (com um tatu!) caso o usuário acesse uma rota que não existe.
* **Foco na Mensagem:** Todas as descrições de status conectam o jargão técnico à causa da preservação.

## Tecnologias Utilizadas

* **Backend:** Python
* **Framework:** Flask
* **Frontend:** HTML5
* **Templates:** Jinja2

## Como Executar Localmente

Siga os passos abaixo para rodar o projeto na sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/http-tatu.git](https://github.com/seu-usuario/http-tatu.git)
    cd http-tatu
    ```

2.  **(Recomendado) Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv
    
    # Ativar no Windows
    .\venv\Scripts\activate
    
    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install Flask
    ```

4.  **Adicione suas imagens:**
    Certifique-se de que suas imagens (ex: `200.jpg`, `404.jpg`, etc.) estão dentro da pasta `static/images/`.

5.  **Rode o aplicativo:**
    ```bash
    # O modo debug recarrega o servidor automaticamente a
