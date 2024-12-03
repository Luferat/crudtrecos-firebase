from flask import flash, g, redirect, render_template, request, url_for
from functions.db_usuario import get_by_email_birth, save_new_password
from functions.geral import gerar_senha


def mod_novasenha(mysql):
    novasenha = ''
    if g.usuario != '':
        return redirect(url_for('perfil'))
    if request.method == 'POST':
        form = dict(request.form)
        row = get_by_email_birth(mysql=mysql, form=form)
        if row == None:
            flash('<h4>Oooops!</h4><p>Não encontrei você! Tente novamente ou cadastre-se.</p>', 'success')
        else:
            novasenha = gerar_senha()
            save_new_password(mysql=mysql, novasenha=novasenha, id=row['u_id'])
    pagina = {
        'titulo': 'CRUDTrecos - Nova Senha',
        'novasenha': novasenha,
    }
    return render_template('novasenha.html', **pagina)
