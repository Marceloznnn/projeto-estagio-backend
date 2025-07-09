from flask import Blueprint, render_template, request

bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if email == 'estagio@gmail.com' and senha == 'estagio2025':
            message = 'Login feito com sucesso!'
        else:
            message = 'E-mail ou senha inválidos.'
    return render_template('login.html', message=message)
