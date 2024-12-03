from flask import flash, g, redirect, render_template, request, url_for
from functions.db_treco import create_treco


def mod_novo(mysql):
    if g.usuario == '':
        return redirect(url_for('login'))
    if request.method == 'POST':
        form = dict(request.form)
        if create_treco(mysql=mysql, form=form):
            flash('<h4>Legal!</h4><p>Seu novo treco foi cadastrado!</p>', 'success')
    pagina = {
        'titulo': 'CRUDTrecos - Novo Treco',
        'usuario': g.usuario,
    }
    return render_template('novo.html', **pagina)
