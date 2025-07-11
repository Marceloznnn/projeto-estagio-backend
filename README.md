# 🔒 Backend - Projeto de Login em Flask

Este é o repositório do **backend** para o projeto de autenticação solicitado pelo professor.  
O objetivo é criar uma aplicação simples em **Python (Flask)** com dois formulários principais:

- ✅ **Login**
- 🔧 **Esqueci minha senha** (ainda a ser implementado)

O frontend será desenvolvido separadamente por outro time, em outro repositório.

---

## 📁 Estrutura do Projeto

```
backend/
├── app/
│   ├── routes/
│   │   ├── __init__.py       # Importa e registra as rotas
│   │   └── login.py          # Rota de login (já implementada)
│   └── templates/            # Templates HTML (se necessário para testes)
├── run.py                    # Arquivo principal para rodar a aplicação
frontend/                     # Diretório externo (não faz parte deste repositório)
```

---

## 🚀 Como executar

1. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

2. **Instale as dependências:**
```bash
pip install flask
```

3. **Execute a aplicação:**
```bash
python run.py
```

A aplicação rodará em:  
📍 [http://localhost:5000](http://localhost:5000)

---

## ✅ Já Implementado

### Login (`POST /`)
- Autenticação simples com email e senha:
  - Email: `estagio@gmail.com`
  - Senha: `estagio2025`
- Exibe mensagens de erro ou sucesso na tela.

---

## 🛠️ O que falta implementar

### 🔐 Esqueci minha senha

Responsável: **Lucas**

Você deve implementar:

- Um formulário com campo de **e-mail** para recuperar a senha.
- Uma rota como: `@bp.route('/esqueci-senha', methods=['GET', 'POST'])`
- Validação do e-mail informado.
- Exibir mensagem do tipo:
  - ✅ “Se o e-mail estiver cadastrado, enviaremos instruções.”
  - ❌ “E-mail inválido.” (opcional)

*Não precisa enviar email real — simule o processo.*

---

## 🤝 Integração com o Frontend

O time de frontend irá consumir estas rotas através de requisições HTTP.  
Garanta que os nomes dos endpoints, métodos e mensagens estejam claros e padronizados.

---

## 📌 Observações

- O projeto está usando **Flask puro**, sem banco de dados neste momento.
- Toda lógica deve estar separada por rotas, com organização clara e reutilizável.

---

## 📃 Requisitos do Professor

-  Backend em Python
-  Login funcional
-  Esqueci a senha funcional
-  Separação entre backend e frontend
-  README para orientar o desenvolvimento

---

## 👥 Time Backend

- **Marcelo** – Responsável pelo Login
- **Lucas** – Responsável pelo Esqueci minha senha#   p r o j e t o - e s t a g i o - b a c k e n d  
 