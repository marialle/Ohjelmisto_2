from flask import Flask, Response
import json
from config import connection


def getAirport(icao):
    sql = f"select name, municipality from airport where ident = '{icao}'";
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


app = Flask(__name__)


@app.route('/kentta/<icao>')
def kentta(icao):
    try:
        airport = getAirport(icao)
        code = 200
        response = {
            "ICAO": icao,
            "Name": airport[0]['name'],
            "Municipality": airport[0]['municipality'],
        }

    except:
        code = 500
        response = {
            "status": code,
            "text": "Error",
            "tip": "Enter a valid ICAO code"
        }

    jsonresp = json.dumps(response)
    return Response(response=jsonresp, status=code, mimetype='application/json')


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)