import json
from flask import g, request


def mod_start(mysql):
    cur = mysql.connection.cursor()
    cur.execute("SET NAMES utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    cur.execute("SET character_set_client=utf8mb4")
    cur.execute("SET character_set_results=utf8mb4")
    cur.execute("SET lc_time_names = 'pt_BR'")
    cookie = request.cookies.get('usuario')
    if cookie:
        g.usuario = json.loads(cookie)
    else:
        g.usuario = ''
