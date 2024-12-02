import json
from flask import g, make_response, redirect, render_template, request, url_for
from functions.db_usuario import get_usuario
from functions.geral import datetime_para_string, remove_prefixo


def mod_login(mysql):
    if g.usuario != '':
        return redirect(url_for('perfil'))
    erro = False
    if request.method == 'POST':
        form = dict(request.form)
        usuario = get_usuario(mysql=mysql, form=form)
        if usuario == None:
            erro = True
        else:
            del usuario['u_senha']
            usuario['u_pnome'] = usuario['u_nome'].split()[0]
            usuario = datetime_para_string(usuario)
            cookie_valor = remove_prefixo(usuario)
            cookie_json = json.dumps(cookie_valor)
            resposta = make_response(redirect(url_for('index')))
            resposta.set_cookie(
                key='usuario',
                value=cookie_json,
                max_age=60 * 60 * 24 * 365
            )
            return resposta
    pagina = {
        'titulo': 'CRUDTrecos - Login',
        'erro': erro
    }
    return render_template('login.html', **pagina)
