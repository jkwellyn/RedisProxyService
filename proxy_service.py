#!/usr/bin/env python3

from flask import Flask, Response, jsonify, request
from flask_api import status
from flask_redis import FlaskRedis
from config import DevelopmentConfig
import cachetools

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())

db = FlaskRedis(app)

expiry = app.config['CAPACITY']
redis_ttl = app.config["TTL"]

cached = cachetools.TTLCache(maxsize=expiry, ttl=redis_ttl)


@app.route('/<key>', methods=['GET'])
def get(key):
    if key in cached:
        return jsonify(cached[key])
    else:
        if db.exists(key):
            redis_result = db.get(key)
            cached[key] = redis_result
            decoded_key = cached[key].decode("utf-8")
            return Response(decoded_key, status=200)
        else:
            print("{} not found".format(key))
            return status.HTTP_404_NOT_FOUND

@app.route('/<key>:<value>', methods=['POST'])
def post(key, value):
    redis_result = db.set(key, value)
    return Response(redis_result, status=201)

@app.route('/<key>', methods=['DELETE'])
def delete(key):
    db.delete(key)

if __name__ == '__main__':
    app.run(host=None, port=None, threaded=True,  processes=3)
