from flask import abort, flash, g, redirect, render_template, request, url_for
from functions.db_treco import get_one_treco, update_treco


def mod_edita(mysql, id):
    if g.usuario == '':
        return redirect(url_for('login'))
    if request.method == 'POST':
        form = dict(request.form)
        update_treco(mysql=mysql, form=form, id=id)
        flash('<h4>Oba!</h4><p>Seu treco foi editado com sucesso!</p>', 'success')
        return redirect(url_for('index'))
    row = get_one_treco(mysql=mysql, id=id)
    if row == None:
        abort(404)
    pagina = {
        'titulo': 'CRUDTrecos',
        'usuario': g.usuario,
        'item': row,
    }
    return render_template('edita.html', **pagina)
