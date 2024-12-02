from flask import g, redirect, render_template, url_for
from functions.db_treco import get_count_user_trecos
from functions.geral import calcular_idade


def mod_perfil(mysql):
    if g.usuario == '':
        return redirect(url_for('login'))
    g.usuario['idade'] = calcular_idade(g.usuario['nascimento'])
    row = get_count_user_trecos(mysql)
    g.usuario['total'] = row['total']
    pagina = {
        'titulo': 'CRUDTrecos - Novo Treco',
        'usuario': g.usuario,
    }
    return render_template('perfil.html', **pagina)
