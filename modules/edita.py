from flask import abort, g, redirect, render_template, request, url_for
from functions.db_treco import get_one_treco, update_treco


def mod_edita(mysql, id):
    if g.usuario == '':
        return redirect(url_for('login'))
    if request.method == 'POST':
        form = dict(request.form)
        update_treco(mysql=mysql, form=form, id=id)
        return redirect(url_for('index', a='editado'))
    row = get_one_treco(mysql=mysql, id=id)
    if row == None:
        abort(404)
    pagina = {
        'titulo': 'CRUDTrecos',
        'usuario': g.usuario,
        'item': row,
    }
    return render_template('edita.html', **pagina)
