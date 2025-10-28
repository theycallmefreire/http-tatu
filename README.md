# HTTP Tatu <img width="45" height="45" alt="logo_sem_texto_lines" src="https://github.com/user-attachments/assets/50dee545-4982-4cce-b77f-39271301baf0" />



Um projeto web que associa códigos de status HTTP a imagens de tatus. Inspirado no `http.cat` e `http.dog`, este app usa Python e Flask para transformar cada erro ou sucesso em um lembrete visual sobre a importância de proteger estes animais.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-black?logo=flask)

---

## A Causa: Por que Tatus?

Eu particularmente adoro tatus!

![508](https://github.com/user-attachments/assets/f8ade6db-ef2c-41ee-9a68-deda57c47433)

---
### Galeria Principal
A página inicial (`/`) exibe todos os códigos de status cadastrados, permitindo uma visualização rápida da galeria e suas descrições.

<img width="1516" height="748" alt="image" src="https://github.com/user-attachments/assets/6ed913b7-f290-4a29-8bec-a69d0884bd3c" />


### Página de Status
Cada código possui uma página dedicada (ex: `/404`) que mostra a imagem em tamanho maior e a descrição daquele status, sempre com a temática da preservação.

<img width="1533" height="755" alt="image" src="https://github.com/user-attachments/assets/9229f161-0b10-4154-b73c-8d79cbe3ba7e" />


## Funcionalidades

* **Galeria de Códigos:** Uma página inicial (`/`) que lista todos os códigos de status implementados.
* **Rotas Dinâmicas:** Acesso a cada código individualmente através de rotas dinâmicas (ex: `/200`, `/404`, `/500`).
* **Templates Jinja2:** Uso de um template base (`base.html`) para criar um layout consistente em todo o site.
* **Página de Erro Personalizada:** O app usa sua própria página de 404 (com um tatu!) caso o usuário acesse uma rota que não existe.

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
4. **Instale requirements**
   ```bash
   pip install -r requirements.txt
   ```
5.  **Rode o aplicativo:**
    ```bash
    flask --app main run
    ```
