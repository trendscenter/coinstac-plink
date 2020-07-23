import subprocess
import json
import sys

def main():
    doc = json.loads(sys.stdin.read())
    cmd = doc['input']['cmd'].split(' ')
    #cmd = './plink --file toy --freq --out toy_analysis'.split(' ')
    result = subprocess.check_output(cmd).decode()
    cmd = 'mv toy_analysis.* ' + doc['state']['outputDirectory']
    subprocess.call(['mv','toy_analysis.*',doc['state']['outputDirectory']])

    computation_output = {
        "output": {
            "output_val": result,
            "computation_phase": 'local0'
        }
    }

    return json.dumps(computation_output)

'''

'''
if __name__ == '__main__':
    main()