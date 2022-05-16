from kubernetes import client, config, watch
import logging
from pydantic import BaseModel
import httpx
import re
import time

url_host = 'http://failuremanager:5002'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


def main():

    
    msg = {"name": "teste 1",
            "type": "teste 2",
            "message": "teste 3",
            "dateevent": "teste4"}

    while True:  
        logging.warning(msg)
        response = httpx.post(f"{url_host}/insufficientcpu",
                                headers=headers,
                                json=msg)

        time.sleep(5000)


if __name__ == '__main__':
    main()
