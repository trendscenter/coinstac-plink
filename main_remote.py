import os
import json
import sys

def main():
    doc = json.loads(sys.stdin.read())
    cmd = [doc['input'][site]["output_val"] for site in doc['input']]

    computation_output = {"output": cmd, "success": True}
    return json.dumps(computation_output)

'''

'''
if __name__ == '__main__':
    main()