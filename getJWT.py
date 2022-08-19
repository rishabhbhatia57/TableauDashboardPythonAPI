import jwt
import datetime
import uuid
from flask import jsonify
ct = datetime.datetime.now()

ct5 = datetime.timedelta(minutes=5)
ts = int(ct.timestamp())
def getJWT():
    print(ct)
    payload = {
    'jti' : str(uuid.uuid4()),
    'iss' : '6e57a52c-6629-4fea-a583-1c6a57983381', # connectedappclientid
    'aud' : 'tableau',
    'sub' : 'Prakash.Khaire', #username
    'scope' : ['tableau:views:embed'], #scope
    "iat": ts,
    'exp' : ts + 300,
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
    print(token)
    return jsonify(token = token)