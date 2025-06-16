from typing import List, Dict, Any
import requests
import os

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

def get_sales(date: str) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    :param date: data retrieve the data from
    :return: list of records
    """
    # TODO: implement me
    headers = {'Authorization': AUTH_TOKEN}
    response = requests.get(f'{API_URL}sales?date={date}&page=1', headers = headers)

    return response.json()

