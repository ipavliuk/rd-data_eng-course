from flask import Flask, request
from flask import typing as flask_typing

from lec02.job2.dal.local_disk import migrate_to_avro

import sys
print("Running with:", sys.executable)


app = Flask(__name__)

@app.route('/', methods = ['POST'])
def main() -> flask_typing.ResponseReturnValue:
    input_data: dict = request.json
    stg_dir = input_data.get('stg_dir')
    raw_dir = input_data.get('raw_dir')

    if not stg_dir:
        return {
            "message": "stg_dir parameter missed",
        }, 400

    if not raw_dir:
        return {
            "message": "raw_dir parameter missed",
        }, 400

    migrate_to_avro(raw_dir, stg_dir)

    return {
        "message": "Data migrated successfully from json to avro",
    }, 201

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='localhost', port=8082)