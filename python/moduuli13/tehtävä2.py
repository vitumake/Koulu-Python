import mysql.connector
from flask import Flask
from json import dumps

with open('./dbpass.txt') as f:
    dbPass = f.readlines()

conn = mysql.connector.connect(
    host='86.115.204.188',
    port= 3306,
    database='rehellinen',
    user='koulu',
    password=dbPass[0],
    autocommit=True,
    auth_plugin='mysql_native_password'
    )
app = Flask(__name__)
@app.route('/kenttä/<icao>')
def alkuluku(icao):
    kursori = conn.cursor(buffered=True)
    kursori.execute(f'SELECT name, municipality FROM airport WHERE ident="{icao}"')
    result = kursori.fetchall()[0]
    return dumps({
        'ICAO':icao,
        'Name':result[0],
        'Municipality':result[1]
    })
if __name__ == '__main__':app.run(use_reloader=True, host='127.0.0.1', port=3000)