import fastavro
import os
import json

avro_schema = {
    "type": "record",
    "name": "SalesRecord",
    "namespace": "com.group.GeneratedAvroSchemaTest",
    "doc": "Sales results",
    "fields": [
        {"name": "client", "type": "string"},
        {"name": "purchase_date", "type": "string"},
        {"name": "product", "type": "string"},
        {"name": "price", "type": "int"},
    ]
}


def migrate_to_avro(src: str, dest: str) -> None:
    os.makedirs(dest, exist_ok=True)

    for file_name in os.listdir(src):
        if not file_name.endswith('.json'):
            continue

        json_path = os.path.join(src, file_name)
        with open(json_path) as json_file:
            data = json.load(json_file)

        avro_path = os.path.join(dest, file_name[:-5] +'.avro')
        with open(avro_path, 'wb') as avro_file:
            fastavro.writer(avro_file, avro_schema, data)


