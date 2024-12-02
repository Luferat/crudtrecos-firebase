from flask import g, make_response, redirect, url_for


def mod_logout():
    if g.usuario == '':
        return redirect(url_for('login'))
    resposta = make_response(redirect(url_for('login')))
    resposta.set_cookie(
        key='usuario',
        value='',
        max_age=0
    )
    return resposta
