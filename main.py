import os
import json
import sys

def main():
    doc = json.loads(sys.stdin.read())
    cmd = './plink ' + '--file toy' + '--freq --out toy_analysis'
    os.system(cmd)
'''

'''
if __name__ == '__main__':
    main()