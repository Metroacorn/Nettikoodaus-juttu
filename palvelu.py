from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello big ol world!</p>"

@app.route("/tulos")
def nayta_tulos():
    luku1 = request.args.get("luku1")
    return try: return "Näiden lukujen summa on %s" % (float(luku1) + float(luku2))
    except: return "EI"


@app.route("/seikkailu")
def nayta_laatikko_sivu():
    return """
        <p>laita tähän kaksi jännittävää lukua:
        <form action="/tulos" enctype="application/x-www-urlencoded"> 
        Eka luku: <input name=luku1 type=text> <br>
        Toka luku: <input name=luku2 type=text> <br>
        <input type=submit value="Tee jotain">
        </form>
"""

@app.route("/boom")
def boom():
    return "boom"

if __name__=="__main__":
    app.run(debug=True)