from flask import Flask, jsonify, request, render_template
# from getJWT import getJWT
from flask_cors import CORS, cross_origin
import jwt
from datetime import datetime
import uuid
import time
import calendar
from flask import jsonify
# from connectedApps import signIntoConnectedApps, getConnectAppsList
import json
from datetime import datetime, timedelta
app = Flask(__name__)
cors = CORS(app)



@app.route('/')
def index():
    return "Python flask is running..."


@app.route('/GetJWT')
def GetJWT():
    ct = datetime.now()
    # pispl_server_time = datetime.now() + timedelta(hours=5, minutes=30) # IST Zone
    ts = int(ct.timestamp())
    # ts = int(pispl_server_time.timestamp())

    payload = {
    'jti' : str(uuid.uuid4()),
    'iss' : 'bc094315-8675-4f6f-b248-4b2317c13f7e', # connectedappclientid
    'aud' : 'tableau',
    'sub' : 'Tableauadmin', #username
    'scope' : ['tableau:views:embed'], #scope
    "iat": ts,
    'exp' : ts + 300,
    }

    signing_key = 'uyznDagevLCgdLGHPva/wySbcknfov4SlEQCvrsN354=' #connectedappsecrectvalue

    algorithm = 'HS256'
    # expiresIn =  datetime.datetime.utcnow() + datetime.timedelta(minutes=5)

    headers = {
        'kid' : 'caca30bf-b586-4176-8312-932a33f98a32', #connectedappsecretid
        'iss' : 'bc094315-8675-4f6f-b248-4b2317c13f7e', #connectedappclientid
    }

    # token = jwt.encode(payload, signing_key, algorithm, headers)
    token = jwt.encode(payload, key=signing_key, algorithm=algorithm, headers=headers,)
    # token = token.decode("utf-8")
    return jsonify(
        token = token,
        issuedAt = datetime.fromtimestamp(ts),
        expireAt = datetime.fromtimestamp(ts + 300)
        )

if __name__ == "__main__":
    app.run(debug=True)
    # app.debug = True

