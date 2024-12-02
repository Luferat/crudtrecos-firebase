from flask import g, redirect, render_template, request, url_for
from functions.db_usuario import get_by_email_birth, save_new_password
from functions.geral import gerar_senha


def mod_novasenha(mysql):
    novasenha = ''
    erro = False
    if g.usuario != '':
        return redirect(url_for('perfil'))
    if request.method == 'POST':
        form = dict(request.form)
        row = get_by_email_birth(mysql=mysql, form=form)
        if row == None:
            erro = True
        else:
            novasenha = gerar_senha()
            save_new_password(mysql=mysql, novasenha=novasenha, id=row['u_id'])
    pagina = {
        'titulo': 'CRUDTrecos - Nova Senha',
        'erro': erro,
        'novasenha': novasenha,
    }
    return render_template('novasenha.html', **pagina)
