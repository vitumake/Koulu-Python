from json import dumps
from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku=int(luku)
    for i in range(luku-1, 0, -1):
        if i==1: prime = True
        elif luku%i==0: 
            prime = False
            break
    return dumps({
        'Number':luku,
        'isPrime':prime
    })
if __name__ == '__main__':app.run(use_reloader=True, host='127.0.0.1', port=3000)