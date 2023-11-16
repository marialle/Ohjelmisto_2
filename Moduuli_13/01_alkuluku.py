from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:

        luku = int(luku)
        result = "true"

        for i in range(2, luku):
            if luku % i == 0:
                result = "false"
                break
            else:
                pass

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "Number": luku,
            "isPrime": result,
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Invalid input",
        }

    jsonresp = json.dumps(vastaus)
    return Response(response=jsonresp, status=tilakoodi, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

# 127.0.0.1:3000/alkuluku/
