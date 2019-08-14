#!/usr/bin/env python3

from flask import Flask, jsonify, request
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
            return decoded_key
        else:
            print("{} not found".format(key))

@app.route('/<key>:<value>', methods=['POST'])
def post(key, value):
    if key in cached:
        print("{} is already saved".format(key))
    elif db.exists(key):
        print("{} is already saved".format(key))

    redis_result = db.set(key, value)
    return redis_result

@app.route('/<key>', methods=['DELETE'])
def delete(key):
    db.delete(key)

if __name__ == '__main__':
    app.run(host=None, port=None, threaded=True,  processes=3)
