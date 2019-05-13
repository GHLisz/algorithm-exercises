# docs: https://foosoft.net/projects/anki-connect/
from typing import List

import json
import os
import requests
from pprint import pprint

from pygments import highlight
from pygments.lexers.python import Python3Lexer
from pygments.formatters.html import HtmlFormatter

HOST_URL = 'http://localhost:8765'


def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}


def invoke(action, **params):
    request_json = json.dumps(request(action, **params))

    response = requests.post(HOST_URL, data=request_json)
    response = response.json()
    # pprint(response)

    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])

    return response['result']


def add_basic_note(deck_name: str, fields_front: str, fields_back: str, tags: 'List[str]'):
    params = {
        "note": {
            "deckName": deck_name,
            "modelName": 'Basic',
            "fields": {
                "Front": fields_front,
                "Back": fields_back,
            },
            "options": {
                "allowDuplicate": False
            },
            "tags": tags,
        }
    }

    invoke('addNote', **params)


# invoke('createDeck', deck='test1')
# result = invoke('deckNames')
# print('got list of decks: {}'.format(result))

def highlight_python(code):
    lexer = Python3Lexer(stripall=True)
    formatter = HtmlFormatter(noclasses=True)
    return highlight(code, lexer, formatter)


def convert_src_file_to_note(fn, deck_name):
    # fn = r"26-remove-duplicates-from-sorted-array.py"

    content = open(fn, encoding='utf8').read()
    q, a = content.split('\n"""\n\n')

    q = q.strip('"""\n')
    q = '<b>' + q.replace('\n', '</b>\n', 1)
    q = q.replace('\n', '<br>')
    q = f'<div align="left">{q}</div>'

    a = highlight_python(a)
    a = f'<div align="left">{a}</div>'

    print('------------')
    print(q)
    print('########')
    print(a)
    print('------------')

    add_basic_note(deck_name, q, a, ['a'])


def main():
    src_path = r"leetcode_tiq\Easy_Array"
    files = os.listdir(src_path)
    files = [os.path.join(src_path, fn) for fn in files]
    # print(*files, sep='\n')
    for fn in files:
        print(f'******processing: {fn} *********')
        convert_src_file_to_note(fn, 'test1')


if __name__ == '__main__':
    fn = r"Easy_Array\36-valid-sudoku.py"
    convert_src_file_to_note(fn, 'Default')
    pass
