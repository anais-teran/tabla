
from flask import Flask, render_template

app = Flask(__name__)

datos = [
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia", "icono": "spotify"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU.", "icono": "netflix"},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU.", "icono": "youtube"},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU.", "icono": "twitch"},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China", "icono": "tiktok"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU.", "icono": "instagram"},
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU.", "icono": "discord"},
]

@app.route('/tabla')
def tabla():
    paises = sorted(list(set([p['pais'] for p in datos])))
    return render_template('tabla.html', datos=datos, paises=paises)

if __name__ == "__main__":
    app.run(debug=True)
