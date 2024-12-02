from flask import g, redirect, render_template, request, url_for
from functions.db_treco import create_treco


def mod_novo(mysql):
    if g.usuario == '':
        return redirect(url_for('login'))
    sucesso = False
    if request.method == 'POST':
        form = dict(request.form)
        if create_treco(mysql=mysql, form=form):
            sucesso = True
    pagina = {
        'titulo': 'CRUDTrecos - Novo Treco',
        'usuario': g.usuario,
        'sucesso': sucesso,
    }
    return render_template('novo.html', **pagina)
