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
    pispl_server_time = datetime.now() + timedelta(hours=5, minutes=30) # IST Zone
    ts = int(ct.timestamp())
    # ts = int(pispl_server_time.timestamp())

    payload = {
    'jti' : str(uuid.uuid4()),
    'iss' : '6e57a52c-6629-4fea-a583-1c6a57983381', # connectedappclientid
    'aud' : 'tableau',
    'sub' : 'Tableauadmin', #username
    'scope' : ['tableau:views:embed'], #scope
    "iat": ts,
    'exp' : ts + 600,
    }

    signing_key = 'AcjrEt0ciZsrDLvs0GADhwgcYc8WM4RvJjaP2STqqlQ=' #connectedappsecrectvalue

    algorithm = 'HS256'
    # expiresIn =  datetime.datetime.utcnow() + datetime.timedelta(minutes=5)

    headers = {
        'kid' : '38bf74c3-344f-47a5-9f5e-1d06a2f9322c', #connectedappsecretid 
        'iss' : '6e57a52c-6629-4fea-a583-1c6a57983381', #connectedappclientid
    }

    # token = jwt.encode(payload, signing_key, algorithm, headers)
    token = jwt.encode(payload, key=signing_key, algorithm=algorithm, headers=headers,)
    # token = token.decode("utf-8")
    return jsonify(
        token = token,
        issuedAt = datetime.fromtimestamp(ts),
        expireAt = datetime.fromtimestamp(ts + 600)
        )

if __name__ == "__main__":
    app.run(debug=True)
    # app.debug = True

