import json


def json_print_pretty(json_file):
    return json.dumps(json_file, sort_keys=True, indent=4, separators=(',', ': '))

def json_get(file_name):
    with open(file_name, 'r') as f:
        return json.loads(f.read())
