from textwrap import indent
from typing import List, Dict, Any
import json

def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    # TODO: implement me
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json_content, f, ensure_ascii=False)

